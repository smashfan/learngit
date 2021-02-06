import pandas as pd
train=pd.read_csv('2021_ICM_Problem_D_Data\influence_data.csv', sep=',')
print(train.describe())
director_count1 = len(set((train['influencer_id']+train['follower_id']).tolist()))
train["add"]=(train['influencer_id']+train['follower_id'])
print(train["add"])
a=set(train['influencer_id'].tolist())|set(train['follower_id'].tolist())
print(len(train['influencer_id'].tolist()))
print(len(set(train['influencer_main_genre'].tolist())))
print(len(a))

