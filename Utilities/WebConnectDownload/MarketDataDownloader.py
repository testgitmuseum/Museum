from Utilities.WebConnectDownload.OptionDownloader import *
from Utilities.WebConnectDownload.DownloadStockMarketData import *
# + rajouter tout ce qu'il y a sur yahoo finance
# + rajouter les inflations etc
# https://github.com/MicroPyramid/forex-python/blob/master/forex_python/converter.py

import datetime

__author__ = 'vfourrier'


class MarketDataDownloader(object):
    def __init__(self, tickers, start_downloading_date=None, end_downloading_date=None):
        self.tickers = tickers
        self.start_downloading_date = start_downloading_date
        self.end_downloading_date = end_downloading_date
        self.df_close_price = None
        self.df_dividend_ost = None
        self.df_historical_dividend = None
        self.name = None
        self.downloader = OptionDownloader(list_ticker=self.tickers)

    def get_multiple_request(self):
        return None

    def get_all_option(self):
        return self.downloader.run()

    def get_option_ask(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_bid(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_implied_vol(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_open_interest(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_percent_change(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_contract_size(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_volume(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_currency(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_moneyness(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_change(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_last(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_option_last_trade_date(self, optionType):
        if optionType == 'call':
            return self.downloader.get_call_ask()
        elif optionType == 'put':
            return self.downloader.get_put_ask()

    def get_close_price(self):
        return 10.0

    def get_stock_data(self):
        return 10.0
