import pandas
import numpy
from datetime import datetime, date
import time

if __name__ == "__main__":
    list_date_exl = pandas.read_csv('./datasource/raw_listing_data.csv')
    list_date_frame = pandas.DataFrame(list_date_exl)
    list_date_frame['listing_show']=list_date_frame['listing_show'].map(str.strip)
    for v in list_date_frame['listing_show']:
        listing_year = 1900
        listing_month = 1
        try:
            if len(v) == 4:
                print(str.isdigit(v))
                listing_year = int(v)
                print(listing_year)
                print(type(v))
        except ValueError:
            print('转型失败 %s' % v)
            continue
       
    # print(list_date_frame)
    pass
