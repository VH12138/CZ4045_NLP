import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.data import load
import pandas as pd
import spacy
import spacy.cli
import en_core_web_lg

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
spacy.cli.download("en_core_web_lg")

stop_words = set(stopwords.words('english'))
json_path = 'reviewSelected100.json'

#Sentence Separation
def sentence_sep(txt_files):
    separated_sentence = []
    for txt_file in txt_files:
        #Tokenize the file into sentences
        sentences = sent_tokenize(str(txt_file))
        #Append sentence to the full dictionary
        for sentence in sentences:
            separated_sentence.append(sentence)
    return separated_sentence

def choose_rand_sen(filename):
    b1review = filename + '.txt'
    file1 = open(b1review, 'r')
    files = list()
    files.append(file1.read())
    #Get all sentences of b1
    b1sentences = sentence_sep(files)
    rand_b1sentences = []
    #choose 5 random sentences from b1sentences
    for i in range(5):
        rand_b1sentences.append(b1sentences[random.randrange(len(b1sentences))])
    return rand_b1sentences

def tagging_nltk(rand_sentences):   
    tagdict = load('help/tagsets/upenn_tagset.pickle')
    for i in rand_sentences:
        print(i)
        text = word_tokenize(i)
        pt = nltk.pos_tag(text)
        data = pd.DataFrame(pt, columns =['Token', 'pos_tag'])
        tags = [t[1] for t in pt]
        tag_meanings = [tagdict[tag] for tag in tags]
        data['Tag meaning'] = tag_meanings
        print('Tagging using NLTK library:')
        print(data,'\n')

def tagging_spacy(rand_sentences):
    nlp = en_core_web_lg.load()
    for i in rand_sentences:
        print(i)
        rows = []
        #text = word_tokenize(i)
        doc = nlp(i)
        for t in doc:
            row = [t.text, t.pos_]
            rows.append(row)
        df = pd.DataFrame(rows, columns =['Token', 'pos_tag'])
        print(df,'\n')

        
if __name__ == '__main__':
    rand_b1sentences = choose_rand_sen('b1review')
    tagging_nltk(rand_b1sentences)
    tagging_spacy(rand_b1sentences)
