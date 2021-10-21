import os
import re
import pandas as pd
import matplotlib.pyplot as plt


def detect_negation(row):
    try:
        text = row['Text']
        negation_words = re.findall(r'(not|\bnever\b|\bno\b|n\'t\W|\Wnon|\bnothing\b|\bnobody\b|\bnowhere\b|\bnope\b)', text, re.IGNORECASE)
        # includes words like: cannot, shouldn't, nontoxic, none, etc.
        return len(negation_words)
    except:
        return 0


inputSubDir = 'result/'
outputSubDir = 'result/'
posts = pd.read_csv(os.path.join(inputSubDir, 'b1review.txt'))
posts['NumNegWords'] = posts.apply(detect_negation, axis=1)
num_posts_with_neg = posts.loc[posts['NumNegWords'] > 0, :].shape[0]
per = num_posts_with_neg * 100.0 / posts.shape[0]

plt.hist(posts['NumNegWords'], bins=range(0, 20, 1), histtype='bar', ec='black')
plt.xlabel('Number of negative words')
plt.ylabel('Number of posts')
plt.title('Negation Expressions count')
plt.text(8, 500, "%d posts (%.2f%%) \nhave negation expressions" % (num_posts_with_neg, per),
         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.savefig(os.path.join(outputSubDir, 'negation_expression_count.png'))
plt.show()