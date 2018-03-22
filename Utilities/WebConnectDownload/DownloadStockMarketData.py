from datetime import datetime
from Utilities.TypeConverter import convert_date_to_int_yahoo_api_format
import json
import requests
import pandas as pd
import urllib2

__author__ = 'vfourrier'

GLOBAL_PATH = r'https://finance.yahoo.com/quote/'
path_results = r'/Volumes/SECURITY 1/Vincent/BSCM/ATM/Results/Data/'

"""
    This class is used to download data related to a single stock or multiple stocks
    Important: Date in yahoo api are calculated as the total number of seconds since
    January 1st 1970 00:00:00.000 
    Use Utilities.TypeConverter to convert your date
         
"""

class DownloadStockMarketData:
    def __init__(self, list_ticker, frequency, start_date, end_date):
        self.global_path = GLOBAL_PATH
        self.list_ticker = list_ticker
        self.frequency = frequency
        self.start_downloading_date = start_date
        self.end_downloading_date = end_date
        self.dict_url = {}
        self.dict_object = {}


    def create_base_stock(self):
        self.get_url()
        self.get_json_from_api()


    def get_json_from_api(self):
        for url in self.dict_url.keys():
            try:
                resp = requests.get(url)
                r = resp.text.encode('utf-8')
                i1 = 0
                i1 = r.find('root.App.main', i1)
                i1 = r.find('{', i1)
                i2 = r.find("\n", i1)
                i2 = r.rfind(';', i1, i2)
                jsonstr = r[i1:i2]
                data = json.loads(jsonstr)
                self.dict_object[ticker] = data
            except:
                self.dict_object[ticker] = 'connection failed'

    def get_url(self):
        interval = self.get_interval(self.frequency)
        temp_yahoo_start_date = convert_date_to_int_yahoo_api_format(self.start_downloading_date)
        temp_yahoo_end_date = convert_date_to_int_yahoo_api_format(self.end_downloading_date)
        if self.start_downloading_date is None and self.end_downloading_date is None:
            for ticker in self.list_ticker:
                self.dict_url[ticker] = self.global_path + ticker
        else:
            for ticker in self.list_ticker:
                self.dict_url[ticker] = self.global_path + ticker +\
                                        '/history?period1=' + temp_yahoo_start_date + '&period2=' +\
                                        temp_yahoo_end_date + '&interval=' + interval + \
                                        '&filter=history&frequency=' + interval

    def get_historical_stock_df_between_dates(self, req_data=None):
        if req_data is None:
            return self.get_all_stock_data()
        else:
            return None
        # get the list of required data for download

    def get_all_stock_data(self):
        return None

    @staticmethod
    def get_interval(frequency):
        if frequency == 'daily':
            return '1d'
        if frequency == 'weekly':
            return '1w'
        if frequency == 'monthly':
            return '1m'

#
# import requests
# import json
# symbol='MSFT'
# url='https://finance.yahoo.com/quote/' + symbol
# resp = requests.get(url)
# r=resp.text.encode('utf-8')
# i1=0
# i1=r.find('root.App.main', i1)
# i1=r.find('{', i1)
# i2=r.find("\n", i1)
# i2=r.rfind(';', i1, i2)
# jsonstr=r[i1:i2]
# data = json.loads(jsonstr)
# name=data['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['shortName']
# price=data['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketPrice']['raw']
# change=data['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketChange']['raw']
# shares_outstanding=data['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['sharesOutstanding']['raw']
# market_cap=data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['marketCap']['raw']
# trailing_pe=data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['trailingPE']['raw']
# earnings_per_share=data['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']['trailingEps']['raw']
# forward_annual_dividend_rate=data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendRate']['raw']
# forward_annual_dividend_yield=data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['dividendYield']['raw']
#
#
# from datetime import datetime
# global_path = r'https://finance.yahoo.com/quote/'
# start_downloading_date = datetime(2018,1,1)
# end_downloading_date = datetime(2018,2,1)
# dict_url = {}
# frequency = 'daily'
# interval = get_interval(frequency)
# temp_yahoo_start_date = convert_date_to_int_yahoo_api_format(start_downloading_date)
# temp_yahoo_end_date = convert_date_to_int_yahoo_api_format(end_downloading_date)
# if start_downloading_date == None and end_downloading_date == None:
#     for ticker in list_ticker:
#         dict_url[ticker] = global_path + ticker
# else:
#     for ticker in list_ticker:
#         dict_url[ticker] = global_path + ticker + '/history?period1=' + str(temp_yahoo_start_date) + '&period2=' + str(temp_yahoo_end_date) + '&interval=' + interval + '&filter=history&frequency=' + interval
#
# list_
# dict_object = {}
# for url in dict_url.keys():
#     try:
#         resp = requests.get(url)
#         r = resp.text.encode('utf-8')
#         i1 = 0
#         i1 = r.find('root.App.main', i1)
#         i1 = r.find('{', i1)
#         i2 = r.find("\n", i1)
#         i2 = r.rfind(';', i1, i2)
#         jsonstr = r[i1:i2]
#         data = json.loads(jsonstr)
#         dict_object[ticker] = data
#     except:
#         dict_object[ticker] = 'connection failed'