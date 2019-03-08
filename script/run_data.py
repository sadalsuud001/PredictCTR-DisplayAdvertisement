import pandas as pd
import numpy as np

def main():
    behavior_data = pd.read_csv('/local/weka/behavior_log.csv')
    btag = pd.get_dummies(behavior_data['btag'])
    
    new_behavior = pd.concat([behavior_data, btag], axis=1, join='outer')
    
    new_behavior = new_behavior.groupby(['user', 'cate']).agg({
        'cart':np.sum,
        'fav':np.sum,
        'pv':np.sum,
        'buy':np.sum
    })
    
    new_behavior.rename(columns={'cate':'cate_id'})
    
    new_behavior.to_csv('/local/weka/new_behavior.csv')
    
#    raw_ad = pd.read_csv('/local/weka/raw_merge_ad.csv', usecols=[1, 2, 3, 4, 6, 7, 10, 11])    
#    
#    final_data = pd.merge(raw_ad, new_behavior, on=['user', 'cate_id'], how='inner')
#    final_data.to_csv('/local/weka/final_data.csv')

    #ad_feature = pd.read_csv('ad_feature.csv')
    #print(ad_feature.head())

if __name__ == "__main__":
    main()