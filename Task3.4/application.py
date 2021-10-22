import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.data import load
import pandas as pd
import spacy
import spacy.cli
import os

# Sentence Separation
def sentence_sep(txt_files):
    separated_sentence = []
    for txt_file in txt_files:
        # Tokenize the file into sentences
        sentences = sent_tokenize(str(txt_file))
        # Append sentence to the full dictionary
        for sentence in sentences:
            separated_sentence.append(sentence)
    return separated_sentence

def findNegation(sentences):
    nlp = spacy.load("en_core_web_lg")
    for i in sentences:
        print(i)
        rows = []
        text = word_tokenize(i)
        doc = nlp(i)
        negation_tokens = [tok for tok in doc if tok.dep_ == 'neg']
        negation_head_tokens = [token.head for token in negation_tokens]
        for token in negation_head_tokens:
            # print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
            # row = [token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children]]
            row = [token.text, [child for child in token.children]]
            rows.append(row)
        df = pd.DataFrame(rows, columns =['Token', 'Negation Expression'])
        print(df,'\n')


if __name__ == '__main__':
    b1review = '../Task3.2/result/b1review.txt'
    file1 = open(b1review, 'r')
    files = list()
    files.append(file1.read())
    # Get all sentences of b1
    b1sentences = sentence_sep(files)
    findNegation(b1sentences)
