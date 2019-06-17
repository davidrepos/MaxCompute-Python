from matplotlib import pyplot
import pandas as pd
import numpy as np
if __name__ == "__main__":
    pdf = pd.DataFrame(pd.read_excel('./datasource/jd_30day.xlsx'))
    # result = pdf.groupby('日期')['引入订单量'].sum()
    # print(result)
    
    pdf.groupby('日期')['引入订单量'].sum().to_excel('./datasource/excel_to_python.xlsx', sheet_name = 'bluewhale_cc')
    unrate =pd.read_excel('./datasource/excel_to_python.xlsx')
    unrate['日期'].replace('-','',regex=True,inplace=True)
    unrate['日期']=unrate['日期'].astype(np.int64)
    ttt = unrate[(unrate['日期'] >= 20190527)&(unrate['日期']<= 20190609)]
    ttt['日期'] = ttt['日期'].astype(np.str)
    #print(unrate)
    pyplot.plot(ttt['日期'],ttt['引入订单量'])
    jd_review = pd.read_excel('./datasource/jd_review.xlsx')
    print(jd_review)
    jd_review['sale_date']=jd_review['sale_date'].astype(np.str)
    pyplot.plot(jd_review['sale_date'],jd_review['_c0'])
    pyplot.show()


    pass