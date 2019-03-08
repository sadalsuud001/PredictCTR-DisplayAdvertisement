import pandas as pd
import numpy as np
import datetime

def main():
    print('Start to handle behavior_log')
    start_time = datetime.datetime.now()
    
    behavior_data = pd.read_csv('behavior_log.csv')
    end1 = datetime.datetime.now()
    print('Got behavior_data, time cost: %d' % (end1-start_time).seconds)
    
    btag = pd.get_dummies(behavior_data['btag'])
    
    new_behavior = pd.concat([behavior_data, btag], axis=1, join='outer')
    new_behavior.rename(columns={'cate':'cate_id'}, inplace=True)
    print(new_behavior.head(5))
    end2 = datetime.datetime.now()
    print('Concate behavior with btag, time cost: %d' % (end2-end1).seconds)
    
    new_behavior = new_behavior.groupby(['user', 'cate_id', 'brand']).agg({
        'cart':np.sum,
        'fav':np.sum,
        'pv':np.sum,
        'buy':np.sum
    })
    end3 = datetime.datetime.now()
    print('Got new behavior, time cost: %d' % (end3-end2).seconds)
    
    print('Start to write csv')
    new_behavior.to_csv('new_behavior.csv')
    end4 = datetime.datetime.now()
    print('End. Total time cost: %d' % (end4-start_time).seconds)
    
#    raw_ad = pd.read_csv('/local/weka/raw_merge_ad.csv', usecols=[1, 2, 3, 4, 6, 7, 10, 11])    
#    
#    final_data = pd.merge(raw_ad, new_behavior, on=['user', 'cate_id'], how='inner')
#    final_data.to_csv('/local/weka/final_data.csv')

    #ad_feature = pd.read_csv('ad_feature.csv')
    #print(ad_feature.head())

if __name__ == "__main__":
    main()