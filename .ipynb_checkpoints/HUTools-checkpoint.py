import pandas as pd
import akshare as ak
import datetime as dt
from dateutil.relativedelta import relativedelta

def getTodayStocks():
    now = dt.datetime.now()
    today = now.strftime("%Y%m%d")
    last_month_date = (now - relativedelta(months = 1)).strftime("%Y%m%d")
    return ak.stock_hot_rank_wc(date=today) # 个股热度
