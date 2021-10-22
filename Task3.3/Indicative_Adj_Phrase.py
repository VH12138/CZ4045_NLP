# ------ Housekeeping ------#
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams
# nltk.download('punkt')
import pandas as pd
# import random
import json
import os
import spacy
from collections import Counter

from POS_tag import sentence_sep

nlp = spacy.load("en_core_web_lg")


class IndicativeAdjPhrase():
    def __init__(self, json_path):
        self.data = pd.read_json(json_path, lines=True, encoding='ISO-8859-1')
        # Randomisation of business b1 is done in previous section, hence skipped here
        self.b1_data = self.data.loc[self.data['business_id'] == 'oICXzFAaUMrYGzjRWmkw4Q']
        self.b1_files = list()
        self.separated_sentence = []
        self.adjective_phrases = []

    # ------ Extraction of b1 reviews from original dataset ------#
    def extract_b1_data(self):
        b1review = self.b1_data['text']
        b1review.to_csv('b1review_AP.txt', header=None, sep='\t', index=False)
        b1_file_temp = open('b1review_AP.txt', "r")
        self.b1_files.append(b1_file_temp.read())

    # ------ Sentence separation for b1 reviews ------#
    def sentence_sep(self):
        for txt_file in self.b1_files:
            # Tokenize the file into sentences
            sentences = sent_tokenize(str(txt_file))
            # Append sentences to the full dictionary
            for sentence in sentences:
                self.separated_sentence.append(sentence)

    # ------ Extraction of b1 AP ------#
    # Note: Spacy's "pos_" tagging is used, where it refers to the coarse-grained part-of-speech from the
    # Universal POS tag set.
    def extract_b1_AP(self):
        for sentence in self.separated_sentence:
            doc = nlp(sentence)
            for i in range(len(doc)):
                if doc[i].pos_ == 'ADV':
                    if doc[i + 1].pos_ == 'ADJ':
                        self.adjective_phrases.append([doc[i].text, doc[i + 1].text])
                    elif doc[i + 1].pos_ == 'VERB' and doc[i + 1].tag_ == 'VBN':
                        self.adjective_phrases.append([doc[i].text, doc[i + 1].text])
                    elif doc[i + 1].pos_ == 'ADV' and doc[i + 2].pos_ == 'ADJ':
                        self.adjective_phrases.append([doc[i].text, doc[i + 1].text, doc[i + 2].text])
                elif doc[i].pos_ == 'ADJ':
                    if doc[i + 1].pos_ == 'ADP':
                        if doc[i + 2].pos_ == 'PRON':
                            self.adjective_phrases.append([doc[i].text, doc[i + 1].text, doc[i + 2].text])
                        elif doc[i + 2].pos_ == 'NOUN':
                            self.adjective_phrases.append([doc[i].text, doc[i + 1].text, doc[i + 2].text])
                    elif doc[i + 1].pos_ == 'ADJ':
                        self.adjective_phrases.append([doc[i].text, doc[i + 1].text])
                # if doc[i].text=='not' and doc[i+1].text=='the' and doc[i+2].pos_=='ADJ':
                # adjective_phrases.append([doc[i].text, doc[i+1].text, doc[i+2].text])
                # if doc[i].text=='one' and doc[i+1].text=='of' and doc[i+2].text=='the' and doc[i+3].pos_=='ADJ':
                # adjective_phrases.append([doc[i].text, doc[i+1].text, doc[i+2].text, doc[i+3].text])

    """
    Definition of AP, examples from b1 reviews, and status of extraction:
    Note: cases without any result are removed

    - Adv + Adj, e.g."pleasantly spicy"
    - Adv + Verb(VBN), e.g."perfectly fried"
    - Adv(RB) + Adv(RB) + Adj, e.g."so eerily quiet"
    - Adj + Prep(ADP) + Noun/Pron, e.g."full of shrimp"
    - Adj + Adj, e.g."fantastic Vietnamese"
    - not + (the +) Adj, e.g."not the best"
    - one of the + Adj, e.g."one of the best"
    """

    # ------ Retrieval of indicative b1 AP ------#
    def indicative_b1_AP(self):
        # Preparation
        other_data = self.data.loc[self.data['business_id'] != 'oICXzFAaUMrYGzjRWmkw4Q']
        # other_data.head(n=3)  # Total: 15200 rows
        otherreview = other_data['text']
        with open('otherreview.txt', 'w', encoding='utf-8') as f:
            f.write(other_data['text'].str.cat(sep='\n'))
        other_file_temp = open('otherreview.txt', "r")
        other_files = list()
        other_files.append(other_file_temp.read())
        other_sentences = sentence_sep(other_files)

        # Count bigrams in other reviews
        other_bigrams = []
        for i in range(len(other_sentences)):
            for item in ngrams(other_sentences[i].split(), 2):
                other_bigrams.append(item)
        counter_bigrams = Counter(other_bigrams)

        # Count trigrams in other reviews
        other_trigrams = []
        for i in range(len(other_sentences)):
            for item in ngrams(other_sentences[i].split(), 3):
                other_trigrams.append(item)
        counter_trigrams = Counter(other_trigrams)

        # Include all bi/trigrams in other reviews and find mismatch (if ever appeared in other reivews then exclude)
        other_bigrams_item = []
        for k, v in counter_bigrams.items():
            other_bigrams_item.append(k)
        other_bigrams_item = [(x.lower(), y.lower()) for x, y in other_bigrams_item]  # Case-insensitive

        other_trigrams_item = []
        for k, v in counter_trigrams.items():
            other_trigrams_item.append(k)
        other_trigrams_item = [(x.lower(), y.lower(), z.lower()) for x, y, z in other_trigrams_item]

        adjective_phrases_lower = [[string.lower() for string in sublist] for sublist in
                                   self.adjective_phrases]  # Case-insensitive
        ap_tuples = [tuple(x) for x in adjective_phrases_lower]

        matched = []
        unique = []
        for i in ap_tuples:
            if i in other_bigrams_item:
                matched.append(i)
            elif i in other_trigrams_item:
                matched.append(i)
            else:
                unique.append(i)
        print("Indicative APs: ", unique)


if __name__ == '__main__':
    json_path = '../Dataset/reviewSelected100.json'  # Modify accordingly if needed
    """
        In total, 121 unique (raw) APs are filtered from comparing b1_reviews and other_reviews. 
        Please refer to the report for detailed analysis.
    """
    IndicativeAdjPhrase_ = IndicativeAdjPhrase(json_path)
    IndicativeAdjPhrase_.extract_b1_data()
    IndicativeAdjPhrase_.sentence_sep()
    IndicativeAdjPhrase_.extract_b1_AP()
    IndicativeAdjPhrase_.indicative_b1_AP()
