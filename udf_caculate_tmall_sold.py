"""
描述：根据总销量 月销量 天销量统计商品的当天销量
作者:大鹏
"""
from datetime import datetime,date,timedelta

# 根据总销量 月销量 计算日销量
def CaculateTmallDailySoldCount(totalSoldHistory:str,dailySoldHistory:str,biz_date:str):
    biz_datetime = datetime.strptime(biz_date,'%Y-%m-%d')
    biz_datetime_before_str =(biz_datetime-timedelta(days=1)).strftime('%Y-%m-%d')
    biz_date_total_count = CaculateTmallTotalSoldCount(totalSoldHistory,biz_date)
    biz_date_total_count_before = CaculateTmallTotalSoldCount(totalSoldHistory,biz_datetime_before_str)
    if biz_date_total_count is not -1 and biz_date_total_count_before is not -1:
        return biz_date_total_count-biz_date_total_count_before
    return CaculateTmallSearchDailySoldCount(dailySoldHistory,biz_date)

# 计算总销量
def CaculateTmallTotalSoldCount(totalSoldHistory:str,biz_date:str):
    if biz_date is None:
        raise ValueError('invalid biz_date')
    if totalSoldHistory is None:
        raise ValueError('invalid argument')
    
    total_count = totalSoldHistory.split(',')
    for key in total_count:
        if key.startswith(biz_date):
            return  int(key.split('|')[1])
    return -1

# 计算月销量
def CaculateTmallMonthSoldCount(monthSoldHistroy:str,biz_date:str):
    if biz_date is None:
        raise ValueError('invalid biz_date')
    if monthSoldHistroy is None:
        raise ValueError('invalid argument')
    month_count = monthSoldHistroy.split(',')
    month_count_no_brackets = [x.replace('[','').replace(']','')  for x in month_count]
    for key in month_count_no_brackets:
        if key.startswith(biz_date):
            return int(key.split('|')[1])
    return -1

# 计算日销量
def CaculateTmallSearchDailySoldCount(dailySoldHistroy:str, biz_date:str):
    if biz_date is None:
        raise ValueError('invalid biz_date')
    if dailySoldHistroy is None or len(dailySoldHistroy)==0:
        return -1
    day_count = dailySoldHistroy.split(',')
    for key in day_count:
        if key.startswith(biz_date):
            return int(key.split('|')[1])
    return -1

if __name__ == "__main__":
    total_str1 = '2019-05-14 11:20:16|0,2019-06-07 18:32:03|8331,'
    daily_str1 = '2019-06-12 15:43:16|2,2019-06-14 22:16:11|-1,'
    sold_count = CaculateTmallDailySoldCount(total_str1,daily_str1,'2019-06-01')

    print(sold_count)

    month_str1 = '[2019-06-08 16:12:11|173],[2019-06-09 04:04:09|165],[2019-06-10 02:21:18|150],[2019-06-11 10:50:57|136],[2019-06-12 00:47:26|122],[2019-06-13 23:29:13|97],[2019-06-14 03:22:08|97],'
    month_count = CaculateTmallMonthSoldCount(month_str1,'2019-06-01')
    print(month_count)

    pass