import pandas as pd
import numpy as np
import datetime

def handleCSV(filepath, targetpath):
    print('start to handle %s' % filepath)
    
    starttime = datetime.datetime.now()
    
    columns = ['user', 'time_stamp', 'btag', 'cate_id', 'brand']
    
    behavior_data = pd.read_csv(filepath, columns)
    behavior_data.columns = columns
    print('Got behavior')
    print(behacior_data.head(5))
    
    btag = pd.get_dummies(behavior_data['btag'])
    
    endtime1 = datetime.datetime.now()
    
    print('Got btag, time costing: %d' % (endtime1 - starttime).seconds)
    print(btag.head(5))
    
    new_behavior = pd.concat([behavior_data, btag], axis=1, join='outer')
    
    new_behavior = new_behavior.groupby(['user', 'cate_id']).agg({
        'cart':np.sum,
        'fav':np.sum,
        'pv':np.sum,
        'buy':np.sum
    })
    endtime2 = datetime.datetime.now()
    print('Got new_behavior, time costing: %d' (endtime2 - endtime1).seconds)
    print(new_behavior.head(5))
    
    print('Begin writing to csv')
    
    new_behavior.to_csv(targetpath)
    
    endtime3 = datetime.datetime.now()
    print('Got csv, time cost: %d' % (endtime3 - endtime2).seconds)

    

def main():
    
    handleCSV('behavior2.csv', 'new_behavior2.csv')
    handleCSV('behavior3.csv', 'new_behavior3.csv')
    handleCSV('behavior4.csv', 'new_behavior4.csv')
    
    
#    raw_ad = pd.read_csv('/local/weka/raw_merge_ad.csv', usecols=[1, 2, 3, 4, 6, 7, 10, 11])    
#    
#    final_data = pd.merge(raw_ad, new_behavior, on=['user', 'cate_id'], how='inner')
#    final_data.to_csv('/local/weka/final_data.csv')

    #ad_feature = pd.read_csv('ad_feature.csv')
    #print(ad_feature.head())

    
if __name__ == "__main__":
    main()