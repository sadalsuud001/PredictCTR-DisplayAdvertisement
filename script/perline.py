# -*- coding: utf-8 -*-
#
import csv
import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

brief1_2 = csv.reader(open('brief1_2.csv', 'rb'))
brief1_2.next()

columns = []
for row in brief1_2:
    start = datetime.datetime.now()
    columns = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
    
    brief3_4 = csv.reader(open('brief3_4_5.csv', 'rb'))
    brief3_4.next()
    for line in brief3_4:
        if row[0] == line[0] and row[1] == line[1] and row[2] == row[2]:
            columns[3] += line[3]
            columns[4] += line[4]
            columns[5] += line[5]
            columns[6] += line[6]
    csv_file = file('brief.csv', 'ab+')
    csv_write = csv.writer(csv_file)
    if os.path.getsize('brief.csv')== 0:
        csv_write.writerow(['user','cate_id','brand','cart','fav', 'pv', 'buy'])
    csv_write.writerow([columns[0],columns[1],columns[2],columns[3],columns[4], columns[5], columns[6]])
    csv_file.close()
    end = datetime.datetime.now()
    print 'Wirte one line, cost: %d' % (end-start).seconds

