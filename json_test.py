# --encoding=utf8--
# coding=utf-8
import json
from datetime import datetime,timedelta
if __name__ == "__main__":
    totalSoldHistory = '2019-05-08 18:37:17|11,2019-05-20 11:13:27|15,2019-06-01 09:31:33|18,'
    dailySoldHistory = ''
    biz_date = '2019-06-16'
    #当天总销量
    biz_date_total_count = -1
    #昨天总销量
    biz_date_total_count_before = -1
    totalSoldHistoryList = list(map(lambda d:d.split('|'),totalSoldHistory.rstrip(',').split(',')))
    totalSoldHistoryList.reverse()
    for kv in totalSoldHistoryList:
        kv_index = totalSoldHistoryList.index(kv)
        sold_count_date = datetime.strptime(kv[0],'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        sold_count_value = kv[1]
        if sold_count_date<=biz_date:
            biz_date_total_count = sold_count_value
            if kv_index != len(totalSoldHistoryList)-1:
                biz_date_total_count_before = totalSoldHistoryList[kv_index+1][1]
            break
    
    print(biz_date_total_count)
    print(biz_date_total_count_before)
    

    if biz_date_total_count is not -1 and biz_date_total_count_before is not -1:
        print(int(biz_date_total_count)-int(biz_date_total_count_before))
    if dailySoldHistory is None or dailySoldHistory =='':
        print(-1)
    daily_count_array = dailySoldHistory.split(',')
    for key in daily_count_array:
        if key.startswith(biz_date):
            print(int(key.split('|')[1]))
    print(-1)
