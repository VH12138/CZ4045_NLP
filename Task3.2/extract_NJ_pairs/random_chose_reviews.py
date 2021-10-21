import json
import random
import pickle


class RandReview(object):
    def __init__(self, path_read, path_write, num_reviews):
        self.path_read = path_read
        self.path_write = path_write
        self.num_reviews = num_reviews
        self.choices = None
        self.star_dict = None
        self.texts = None

    def read_text(self):
        with open(self.path_read) as f:
            self.star_dict = json.load(f)
        dict_len = len(self.star_dict)
        self.choices = random.sample([i for i in range(0, dict_len)], self.num_reviews)
        self.choices.sort()

    def select_rand_reviews(self):
        count = 0
        self.texts = []
        for i, (business_id, text_list) in enumerate(self.star_dict.items()):
            if i == self.choices[0]:
                self.choices.pop(0)
                count += 1
                rand_n = random.randint(0, len(text_list) - 1)
                self.texts.append(text_list[rand_n])
                if len(self.choices) == 0:
                    break
            else:
                continue
        assert count == self.num_reviews

    def write_selected_reviews_pickle(self):
        pickle.dump(self.texts, open(self.path_write, "wb"))


if __name__ == '__main__':
    path_read = '../../../NLPproject1/processedData/text_grpbsid_star3.json'
    path_write = '../../../NLPproject1/pickle_data/texts_star3.p'
    myRandReview = RandReview(path_read, path_write, 20)
    myRandReview.read_text()
    myRandReview.select_rand_reviews()
    myRandReview.write_selected_reviews_pickle()