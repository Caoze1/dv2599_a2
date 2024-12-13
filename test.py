import pandas as pd
import numpy as np
import statistics as stat

import random

d = {
    'Fold':[1,2,3,4,5,6,7,8,9,10,'avg', 'stdev'],
    'Naive Bayes':[0.6809 , 0.7017, 0.7012, 0.6913, 0.6333, 0.6415, 0.7216, 0.7214, 0.6578, 0.7865, 0.6937, .0448],
    'Decision tree':[0.7524, 0.8964, 0.6803, 0.9102, 0.7758, 0.8154, 0.6224, .7585, .9380, .7524, 0.7902, .1014],
    'Nearest neighbour':[.7164,.8883,.8410,.6825,.7599,.8479,.7012,.4959,.9279,.7455, .7606, .1248],
}

df_friedman = pd.DataFrame({'Data set':[1,2,3,4,5,6,7,8,9,10, 'avg rank']})
df_scores = pd.DataFrame(d)

### Remove last two rows and fold column
df_scores = df_scores.iloc[:-2]
df_rank = df_scores.drop(columns='Fold')

### Rank
df_rank = df_rank.rank(1, 'max', ascending=False)

### Add avg_rank row
df_rank_avg = df_rank.mean()

### Combine ranks and score values
df_scores = df_scores.rename(columns={'Fold': 'Data set'})
for column in df_rank.columns:
    combines = [f"{x} ({int(y)})" for x, y in zip(df_scores[column], df_rank[column])]
    df_scores[column] = combines

df_scores.loc[len(df_scores)] = ['avg rank', df_rank_avg.iloc[0], df_rank_avg.iloc[1], df_rank_avg.iloc[2]] 


print(df_scores)
 

