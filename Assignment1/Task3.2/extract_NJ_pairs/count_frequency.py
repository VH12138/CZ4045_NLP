import pandas as pd


def get_top_frequenct_nj_pairs(path):
    df = pd.read_csv(path)
    freq_df = df.groupby(["Noun", "Adj"]).size().reset_index(name="Time")
    freq_df = freq_df.sort_values(by=["Time"], ascending=False)
    print(freq_df[:10])


if __name__ == '__main__':
    path = "../../../NLPproject1/result/noun_adj_star3.csv"
    get_top_frequenct_nj_pairs(path)