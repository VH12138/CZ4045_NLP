import pandas as pd
import json
import os

def generate_json_grpby_bsid_diff_star(filepath: '', save_folder: ''):
    """
    This is preprocess function to generate separate data file for each star, from 1 to 5.
    Each json file contains onlu
    :return: None
    """
    df = pd.read_json(filepath, lines=True, encoding='ISO-8859-1')

    for i in range(1, 6):
        print("Generating data group by business id with star: " + str(i))
        star_df = df[df['stars'] == i]

        bsid_unique_star = star_df.business_id.unique()
        print("For " + "star 1. There are " + str(len(bsid_unique_star)) + " unique business.")

        # choose only the business id and text from star_df and save to json file

        text_grpbsid_star = dict()
        for id in bsid_unique_star:
            id_text_list = star_df[star_df['business_id'] == id].text.tolist()
            text_grpbsid_star[id] = id_text_list

        save_path = save_folder + '/' + 'text_grpbsid_star'+str(i)+'.json'

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(text_grpbsid_star, f, ensure_ascii=False, indent=4)
        print(save_path + ' is saved')


if __name__ == '__main__':
    filepath = '../../Dataset/reviewSelected100.json'
    if not os.path.exists('../extract-NJ-pairs/processedData'):
        os.makedirs('../extract-NJ-pairs/processedData')
    save_folder = 'processedData'
    generate_json_grpby_bsid_diff_star(filepath, save_folder)
