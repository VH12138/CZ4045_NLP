from extract_NJ_pairs.count_frequency import get_top_frequenct_nj_pairs
from extract_NJ_pairs.random_chose_reviews import RandReview
from extract_NJ_pairs.extract_nj_pair import TextPreprocessor, NounAdjPair
from extract_NJ_pairs.groupbybsid_withstar import generate_json_grpby_bsid_diff_star
import pickle
import pandas as pd
import os

if __name__ == '__main__':
    STAR = '5'  # Change this star parameter if needed

    if not os.path.exists('extract_NJ_pairs/processedData'):
        filepath = '../Dataset/reviewSelected100.json'
        os.makedirs('extract_NJ_pairs/processedData')
        save_folder = 'extract_NJ_pairs/processedData'
        generate_json_grpby_bsid_diff_star(filepath, save_folder)

    if STAR == '1':
        no_review = 50
    else:
        no_review = 20
    if not os.path.exists('extract_NJ_pairs/processedData/pickle_data'):
        os.makedirs('extract_NJ_pairs/processedData/pickle_data')

    path_read = 'extract_NJ_pairs/processedData/text_grpbsid_star' + STAR + '.json'
    path_write = 'extract_NJ_pairs/processedData/pickle_data/texts_star' + STAR + '.p'
    myRandReview = RandReview(path_read, path_write, no_review)
    myRandReview.read_text()
    myRandReview.select_rand_reviews()
    myRandReview.write_selected_reviews_pickle()

    texts_star1 = pickle.load(open('extract_NJ_pairs/processedData/pickle_data/texts_star' + STAR + '.p', 'rb'))
    pairs_list = []
    for text in texts_star1:
        myTextPreprocessor = TextPreprocessor(text)

        myNounAdjPair = NounAdjPair(myTextPreprocessor.sentences, myTextPreprocessor.taggings)
        pairs = myNounAdjPair.get_pairs_one_text()
        pairs_list += pairs
    df = pd.DataFrame(pairs_list, columns=['Noun', 'Adj'])
    df.to_csv('result/noun_adj_star' + STAR + '.csv', index=False)

    path = 'result/noun_adj_star' + STAR + '.csv'
    get_top_frequenct_nj_pairs(path)
