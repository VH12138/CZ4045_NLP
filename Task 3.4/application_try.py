import os
import re
import pandas as pd
import matplotlib.pyplot as plt

from POS_tag import sentence_sep


def detect_negation(b1sentences_):
    negation_words_dict = {}
    for text in b1sentences_:
        negation_word = re.findall(r'(not|\bnever\b|\bno\b|n\'t\W|\Wnon|\bnothing\b|\bnobody\b|\bnowhere\b|\bnope\b)',
                                    text, re.IGNORECASE)
        # if len(negation_word) != 0:
        #     print(text)
        for word in negation_word:
            word = word.lower()
            word = " ".join(re.split("[^a-zA-Z]*", word))
            if word == " n  t  ":
                word = "n\'t"
            if word not in negation_words_dict:
                print(word)
                print(len(word))
                negation_words_dict[word] = 1
            else:
                negation_words_dict[word] += 1
    return negation_words_dict


if __name__ == '__main__':
    b1review = '../Task3.2/result/b1review.txt'
    file1 = open(b1review, 'r')
    files = list()
    files.append(file1.read())
    b1sentences = sentence_sep(files)

    negation_words_dict_ = detect_negation(b1sentences)

    plt.bar(list(negation_words_dict_.keys()), negation_words_dict_.values(), color='grey')
    plt.show()


