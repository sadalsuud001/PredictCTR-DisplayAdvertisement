import pandas as pd
import numpy as np
import datetime

def main():
    starttime = datetime.datetime.now()
    print('Read five csv')
    brief1 = pd.read_csv('brief1_2.csv')
    brief2 = pd.read_csv('brief3_4_5.csv')
    end1 = datetime.datetime.now()
    print('Got behavior brief 1, time cost: %d' % (end1-starttime).seconds)
    
    print('merge 12 & 345')
    brief1_2 = pd.concat([brief1, brief2], axis=0, join='outer')
    brief1_2 = brief1_2.groupby(['user', 'cate_id', 'brand']).agg({
        'cart':np.sum,
        'fav':np.sum,
        'pv':np.sum,
        'buy':np.sum
    })
    end2 = datetime.datetime.now()
    print('Got brief1_2, time cost: %d' % (end2-end1).seconds)
    
    
    
    print('TO csv')
    brief1_2.to_csv('final.csv')
    end6 = datetime.datetime.now()
    print('end total cost: %d' % (end6-starttime).seconds)
    
if __name__ == "__main__":
    main()
    

from sagemaker import get_execution_role

# connect to s3
role = get_execution_role()
bucket='281data'

import pandas as pd
import numpy as np
from sagemaker.amazon.common import write_numpy_to_dense_tensor
import io
import boto3
import datetime

brief1 = 's3://{}/brief1_2.csv'.format(bucket)
brief2 = 's3://{}/brief3_4_5.csv'.format(bucket)

out_path = 's3://{}/final.csv'.format(bucket)
starttime = datetime.datetime.now()

brief1_data = pd.read_csv(brief1)
brief2_data = pd.read_csv(brief2)
end1 = datetime.datetime.now()
print('Got behavior brief 1, time cost: %d' % (end1-starttime).seconds)

print('merge 12 & 345')
brief1_data = pd.concat([brief1_data, brief2_data], axis=0, join='outer')
brief1_data = brief1_data.groupby(['user', 'cate_id', 'brand']).agg({
    'cart':np.sum,
    'fav':np.sum,
    'pv':np.sum,
    'buy':np.sum
})
end2 = datetime.datetime.now()
print('Got brief1_2, time cost: %d' % (end2-end1).seconds)

print('TO csv')
csv_buffer = StringIO()
end2.to_csv(csv_buffer, index=False)
boto3.resource('s3').Bucket(bucket).Object('out').put(Body=csv_buffer.getvalue())