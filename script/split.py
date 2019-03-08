# -*- coding: utf-8 -*-
# 
import os
import sys
import csv
 
# initla encoding
reload(sys)
sys.setdefaultencoding('utf-8')
 
# read csv
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'csv','behavior_log.csv')
csv_reader = csv.reader(open(csv_path,'rb'))
csv_reader.next()
i=j=1
for row in csv_reader:
	if i%50000000==0:
		print u"CSV文件source%s已生成成功" % j
		j+=1
	# write csv
	csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'csv','source'+str(j)+'.csv')
	csv_file = file(csv_path, 'ab+')
	csv_write = csv.writer(csv_file)
	# write header	
	if os.path.getsize(csv_path)==0:
		csv_write.writerow(['user','time_stamp','btag','cate_id','brand'])
	# write data
	csv_write.writerow([row[0],row[1],row[2],row[3],row[4]])
	csv_file.close()
	i+=1
# close