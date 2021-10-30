import nltk
import random
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import os

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

stop_words = set(stopwords.words('english'))
json_path = '../Dataset/reviewSelected100.json'


def extractData(filename):
    data = pd.read_json(json_path, lines=True, encoding='ISO-8859-1')
    biz = data['business_id'].unique()
    biz_choice = random.choice(biz)
    b1_data = data.loc[data['business_id'] == biz_choice]
    b1review = b1_data['text']
    b1review.to_csv('result/'+str(filename) + '.txt')


def tokenize_library(inputtxt_files):
    # Create a token library
    token_library = {}
    # Set tokenizer to only regex words
    tokenizer = RegexpTokenizer(r'\w+')
    # Loop for each file
    for i in inputtxt_files:
        # Tokenized contains the words converted to lower letters
        tokenized = tokenizer.tokenize(i.lower())
        # Loop for each token
        for j in tokenized:
            if j.isdigit():
                # ignore number tokens
                pass
            else:
                # If token has not been added to library before and not stop words
                if j.lower() not in token_library and j.lower() not in stop_words:
                    # Add token to dictionary
                    token_library[j.lower()] = 1
                # if token has been added before and not stop words
                elif j.lower() not in stop_words:
                    # Add 1 more occurance to dictionary
                    token_library[j.lower()] += 1
    # sort the token library by frequency
    sorted_dict = dict(sorted(token_library.items(),
                              key=lambda item: item[1],
                              reverse=True))
    return sorted_dict


def stemming(lib):
    porter_stemmer = PorterStemmer()
    # Initialize new dict
    stemm_dict = {}
    # Loop for each item in dictionary
    for word in lib:
        stemmed_w = porter_stemmer.stem(word)

        if stemmed_w not in stemm_dict:
            stemm_dict[stemmed_w] = 1
        else:
            stemm_dict[stemmed_w] += 1

    stemm_dict = dict(sorted(stemm_dict.items(),
                             key=lambda item: item[1],
                             reverse=True))
    return stemm_dict


def getLengthDict(business_dict):
    # create a counter dictionary
    counter = {}
    # get length of each word's occurance times
    for word in business_dict:
        if len(word) not in counter:
            counter[len(word)] = 1
        else:
            counter[len(word)] += 1
    return counter


def wordFrequency(before_lib, after_lib, png_name):
    plt.figure(figsize=(20, 10))
    D = getLengthDict(before_lib)

    plt.bar(range(len(D)), list(D.values()), align='center', alpha=0.5, label="Before Stemming", edgecolor='black',
            hatch="/")
    plt.xticks(range(len(D)), list(D.keys()))
    plt.xticks(rotation=90)

    ## after stemming
    D = getLengthDict(after_lib)

    plt.bar(range(len(D)), list(D.values()), align='center', alpha=0.5, label="After Stemming", edgecolor='black',
            hatch=".")
    plt.xticks(range(len(D)), list(D.keys()))
    plt.xticks(rotation=90)
    plt.ylabel('count')
    plt.xlabel('length')
    plt.title('Length distribution of tokens')
    plt.legend(prop={'size': 40})

    plt.savefig('result/'+ str(png_name) + '.png')
    # plt.show()

def reviewData(filename, png_name):
    b1review = 'result/'+filename + '.txt'
    file1 = open(b1review, 'r')
    files = list()
    files.append(file1.read())
    b1tokens_lib = tokenize_library(files)
    print('------Before Stemming------')
    print()
    print('Tokens for Data:\n')
    print(b1tokens_lib)
    print()
    print('Top-10 most frequent words before stemming:\n')
    print(list(b1tokens_lib)[:10])
    print()
    print('------After Stemming------')
    b1stemm_dict = stemming(b1tokens_lib)
    print()
    print('Tokens for Data:\n')
    print(b1stemm_dict)
    print()
    print('Top-10 most frequent words after stemming:\n')
    print(list(b1stemm_dict)[:10])
    # Comparision
    print("Total unique tokens before stemming: " + str(len(b1tokens_lib)))
    print("Total unique tokens after stemming: " + str(len(b1stemm_dict)))
    wordFrequency(b1tokens_lib, b1stemm_dict, png_name)


if __name__ == '__main__':
    if not os.path.exists('result'):
        os.makedirs('result')
    extractData('b1review')
    extractData('b2review')
    print('Word frequency distributions for b1:')
    reviewData('b1review', 'b1_word_frequency')
    print('Word frequency distributions for b2:')
    reviewData('b2review', 'b2_word_frequency')
