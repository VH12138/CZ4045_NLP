import pickle
import spacy
import re
import nltk
from nltk.tokenize import sent_tokenize
import en_core_web_sm
nlp = spacy.load("en_core_web_sm")
import pandas as pd


class TextPreprocessor(object):
    def __init__(self, text):
        self.original_doc = text
        self.mytext = self.get_mytext()
        self.original_sentences = self.get_original_sentences()
        self.sentences = self.get_sentences()
        self.taggings = self.get_taggings()

    def get_mytext(self):
        return re.sub(' +', ' ', self.original_doc.replace('\n', ' ').strip()).lower()

    def get_original_sentences(self):
        return [s for s in sent_tokenize(self.mytext)]  # nltk tokenizer

    def get_sentences(self):
        return [' '.join([w.text for w in nlp(s)]) for s in self.original_sentences]  # spacy word tokenizer

    def get_taggings(self):
        return [' '.join([w.pos_ for w in nlp(s)]) + ' ' for s in self.original_sentences]


class NounAdjPair(object):
    def __init__(self, beauty_sentence_list, taggings):
        self.beauty_sentence_list = beauty_sentence_list
        self.taggings = taggings
        self.index_arr = None

    def get_pairs_one_text(self):
        pairs = []
        for i in range(len(self.beauty_sentence_list)):
            one_sentence = self.beauty_sentence_list[i].strip().split(' ')
            one_raw_tagging = self.taggings[i].strip().split(' ')
            self.find_index_adj_noun(one_tagging_=one_raw_tagging)
            pairs += self.get_adj_noun_pair(one_sentence_=one_sentence)
        return pairs

    def find_index_adj_noun(self, one_tagging_):
        self.index_arr = []
        for j in range(len(one_tagging_) - 1):
            if one_tagging_[j] == 'ADJ' and one_tagging_[j + 1] == 'NOUN':  # pattern1 ADJ NOUN
                if (j + 2) < len(one_tagging_) - 1 and one_tagging_[j + 2] == 'NOUN':  # pattern2 ADJ NOUN NOUN
                    self.index_arr.append([2, j, j + 1, j + 2])
                else:
                    self.index_arr.append([1, j, j + 1])
            elif one_tagging_[j] == 'ADJ' and one_tagging_[j + 1] == 'ADJ':
                if (j + 2) < len(one_tagging_) - 1 and one_tagging_[j + 2] == 'NOUN':  # pattern3 ADJ ADJ NOUN
                    self.index_arr.append([3, j, j + 1, j + 2])

    def get_adj_noun_pair(self, one_sentence_):
        adj_noun_pair_list = []
        for index in self.index_arr:
            if index[0] == 2:  # pattern ADJ NOUN NOUN
                pair_tuple = one_sentence_[index[1]], one_sentence_[index[2]] + ' ' + one_sentence_[index[3]]
            elif index[0] == 1:  # pattern1 ADJ NOUN
                pair_tuple = (one_sentence_[index[1]], one_sentence_[index[2]])
            else:  # pattern3 ADJ ADJ NOUN
                pair_tuple = one_sentence_[index[1]] + ' ' + one_sentence_[index[2]], one_sentence_[index[3]]
            adj_noun_pair_list.append(pair_tuple)
        return adj_noun_pair_list


if __name__ == '__main__':
    # import nltk
    # import ssl
    #
    # try:
    #     _create_unverified_https_context = ssl._create_unverified_context
    # except AttributeError:
    #     pass
    # else:
    #     ssl._create_default_https_context = _create_unverified_https_context
    # nltk.download('punkt')
    texts_star1 = pickle.load(open('../../../NLPproject1/pickle_data/texts_star3.p', 'rb'))
    pairs_list = []
    for text in texts_star1:
        myTextPreprocessor = TextPreprocessor(text)

        myNounAdjPair = NounAdjPair(myTextPreprocessor.sentences, myTextPreprocessor.taggings)
        pairs = myNounAdjPair.get_pairs_one_text()
        pairs_list += pairs
    df = pd.DataFrame(pairs_list, columns=['Noun', 'Adj'])
    df.to_csv('result/noun_adj_star3.csv', index=False)
