from datetime import datetime
import json
import pandas as pd
import urllib2

__author__ = 'vfourrier'

GLOBAL_PATH = r'https://query2.finance.yahoo.com/v7/finance/options/'
list_params_options = ['impliedVolatility', 'openInterest', 'percentChange', 'contractSize', 'volume', 'currency',
                       'inTheMoney', 'change', 'ask', 'bid', 'lastPrice', 'lastTradeDate']
path_results = r'/Volumes/SECURITY 1/Vincent/BSCM/ATM/Results/Data/'

"""
    This class is used to download data related to the option market including
    option chain, prices, implied volatility etc 
    Request is made from yahoo finance (google finance will be implemented)
    Use:
        from Utilities.WebConnectDownload.OptionDownloader import *
        ...
        downloader = OptionDownloader(list_of_your_ticker)
        name_of_your_variable = downloader.run() to get all the df
        or
        name_of_your_variable = downloader.get_+somthin()
    list of methods get available:
        get_(write_option_type:call or put)_implied_vol()
        get_(write_option_type:call or put)_open_interest()
        get_(write_option_type:call or put)_percent_change()
        get_(write_option_type:call or put)_contract_size()
        get_(write_option_type:call or put)_volume()
        get_(write_option_type:call or put)_currency()
        get_(write_option_type:call or put)_moneyness()
        get_(write_option_type:call or put)_change()
        get_(write_option_type:call or put)_ask()
        get_(write_option_type:call or put)_bid()
        get_(write_option_type:call or put)_last_price()
        get_(write_option_type:call or put)_last_trade_date()     
"""


class OptionDownloader(object):
    def __init__(self, list_ticker):
        self.global_path = GLOBAL_PATH
        self.list_ticker = list_ticker
        self.dict_url = {}
        self.dict_object = {}
        self.dict_results = {}
        self.dict_quote = {}
        self.dict_calls = {}
        self.dict_puts = {}
        self.dict_call_implied_vol = {}
        self.df_option_quote = None
        self.df_call_option = None
        self.df_put_option = None
        self.dict_call_implied_vol = {}
        self.dict_call_open_interest = {}
        self.dict_call_percent_change = {}
        self.dict_call_contract_size = {}
        self.dict_call_volume = {}
        self.dict_call_currency = {}
        self.dict_call_moneyness = {}
        self.dict_call_change = {}
        self.dict_call_ask = {}
        self.dict_call_bid = {}
        self.dict_call_last_price = {}
        self.dict_call_last_trade_date = {}
        self.dict_put_implied_vol = {}
        self.dict_put_open_interest = {}
        self.dict_put_percent_change = {}
        self.dict_put_contract_size = {}
        self.dict_put_volume = {}
        self.dict_put_currency = {}
        self.dict_put_moneyness = {}
        self.dict_put_change = {}
        self.dict_put_ask = {}
        self.dict_put_bid = {}
        self.dict_put_last_price = {}
        self.dict_put_last_trade_date = {}
        self.list_params_options = list_params_options
        self.get_url()
        self.get_data_json()
        self.get_dict_results()

    def run(self):
        self.get_option_quote_info()
        self.dict_calls = self.get_dict_calls()
        self.dict_puts = self.get_dict_puts()
        self.df_option_quote = self.create_df_data(self.dict_quote, self.list_ticker)
        self.create_df_individual_params_call()
        self.create_df_individual_params_put()
        self.create_df_option()
        self.dump_results()

    def get_call_implied_vol(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_implied_vol = self.create_dict_params_options('calls', 'impliedVolatility')
        list_params_options = ['impliedVolatility']
        return self.create_df_all_params(self.dict_call_implied_vol, list_params_options=list_params_options)

    def get_call_open_interest(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_open_interest = self.create_dict_params_options('calls', 'openInterest')
        list_params_options = ['openInterest']
        return self.create_df_all_params(self.dict_call_open_interest, list_params_options=list_params_options)

    def get_call_percent_change(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_percent_change = self.create_dict_params_options('calls', 'percentChange')
        list_params_options = ['percentChange']
        return self.create_df_all_params(self.dict_call_percent_change, list_params_options=list_params_options)

    def get_call_contract_size(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_contract_size = self.create_dict_params_options('calls', 'contractSize')
        list_params_options = ['contractSize']
        return self.create_df_all_params(self.dict_call_contract_size, list_params_options=list_params_options)

    def get_call_volume(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_volume = self.create_dict_params_options('calls', 'volume')
        list_params_options = ['volume']
        return self.create_df_all_params(self.dict_call_volume, list_params_options=list_params_options)

    def get_call_currency(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_currency = self.create_dict_params_options('calls', 'currency')
        list_params_options = ['currency']
        return self.create_df_all_params(self.dict_call_currency, list_params_options=list_params_options)

    def get_call_moneyness(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_moneyness = self.create_dict_params_options('calls', 'inTheMoney')
        list_params_options = ['inTheMoney']
        return self.create_df_all_params(self.dict_call_moneyness, list_params_options=list_params_options)

    def get_call_change(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_change = self.create_dict_params_options('calls', 'change')
        list_params_options = ['change']
        return self.create_df_all_params(self.dict_call_change, list_params_options=list_params_options)

    def get_call_ask(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_ask = self.create_dict_params_options('calls', 'ask')
        list_params_options = ['ask']
        return self.create_df_all_params(self.dict_call_ask, list_params_options=list_params_options)

    def get_call_bid(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_bid = self.create_dict_params_options('calls', 'bid')
        list_params_options = ['bid']
        return self.create_df_all_params(self.dict_call_bid, list_params_options=list_params_options)

    def get_call_last_price(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_last_price = self.create_dict_params_options('calls', 'lastPrice')
        list_params_options = ['lastPrice']
        return self.create_df_all_params(self.dict_call_last_price, list_params_options=list_params_options)

    def get_call_last_trade_date(self):
        self.dict_calls = self.get_dict_calls()
        self.dict_call_last_trade_date = self.create_dict_params_options('calls', 'lastTradeDate')
        list_params_options = ['lastTradeDate']
        return self.create_df_all_params(self.dict_call_last_trade_date, list_params_options=list_params_options)

    def get_put_implied_vol(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_implied_vol = self.create_dict_params_options('puts', 'impliedVolatility')
        list_params_options = ['impliedVolatility']
        return self.create_df_all_params(self.dict_put_implied_vol, list_params_options=list_params_options)

    def get_put_open_interest(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_open_interest = self.create_dict_params_options('puts', 'openInterest')
        list_params_options = ['openInterest']
        return self.create_df_all_params(self.dict_put_open_interest, list_params_options=list_params_options)

    def get_put_percent_change(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_percent_change = self.create_dict_params_options('puts', 'percentChange')
        list_params_options = ['percentChange']
        return self.create_df_all_params(self.dict_put_percent_change, list_params_options=list_params_options)

    def get_put_contract_size(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_contract_size = self.create_dict_params_options('puts', 'contractSize')
        list_params_options = ['contractSize']
        return self.create_df_all_params(self.dict_put_contract_size, list_params_options=list_params_options)

    def get_put_volume(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_volume = self.create_dict_params_options('puts', 'volume')
        list_params_options = ['volume']
        return self.create_df_all_params(self.dict_put_volume, list_params_options=list_params_options)

    def get_put_currency(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_currency = self.create_dict_params_options('puts', 'currency')
        list_params_options = ['currency']
        return self.create_df_all_params(self.dict_put_currency, list_params_options=list_params_options)

    def get_put_moneyness(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_moneyness = self.create_dict_params_options('puts', 'inTheMoney')
        list_params_options = ['inTheMoney']
        return self.create_df_all_params(self.dict_put_moneyness, list_params_options=list_params_options)

    def get_put_change(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_change = self.create_dict_params_options('puts', 'change')
        list_params_options = ['change']
        return self.create_df_all_params(self.dict_put_change, list_params_options=list_params_options)

    def get_put_ask(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_ask = self.create_dict_params_options('puts', 'ask')
        list_params_options = ['ask']
        return self.create_df_all_params(self.dict_put_ask, list_params_options=list_params_options)

    def get_put_bid(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_bid = self.create_dict_params_options('puts', 'bid')
        list_params_options = ['bid']
        return self.create_df_all_params(self.dict_put_bid, list_params_options=list_params_options)

    def get_put_last_price(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_last_price = self.create_dict_params_options('puts', 'lastPrice')
        list_params_options = ['lastPrice']
        return self.create_df_all_params(self.dict_put_last_price, list_params_options=list_params_options)

    def get_put_last_trade_date(self):
        self.dict_puts = self.get_dict_puts()
        self.dict_put_last_trade_date = self.create_dict_params_options('puts', 'lastTradeDate')
        list_params_options = ['lastTradeDate']
        return self.create_df_all_params(self.dict_put_last_trade_date, list_params_options=list_params_options)

    def get_url(self):
        for ticker in self.list_ticker:
            self.dict_url[ticker] = self.global_path + ticker

    def get_data_json(self):
        for ticker in self.dict_url.keys():
            try:
                temp_ = urllib2.urlopen(self.dict_url[ticker])
            except Exception:
                continue
            self.dict_object[ticker] = json.load(temp_)

    def get_dict_results(self):
        for ticker in self.dict_object.keys():
            self.dict_results[ticker] = self.dict_object[ticker]['optionChain']['result'][0]

    def get_option_quote_info(self):
        for ticker in self.dict_results.keys():
            for key in self.dict_results[ticker].keys():
                if key == 'quote':
                    temp_dict_ = {}
                    for key_ in self.dict_results[ticker][key].keys():
                        temp_dict_[key_] = self.dict_results[ticker][key][key_]
                    self.dict_quote[ticker] = temp_dict_

    def get_dict_calls(self):
        return self.create_dict_data_option(self.dict_results, 'calls')

    def get_dict_puts(self):
        return self.create_dict_data_option(self.dict_results, 'puts')

    def create_df_individual_params_call(self):
        self.dict_call_implied_vol = self.create_dict_params_options('calls', 'impliedVolatility')
        self.dict_call_open_interest = self.create_dict_params_options('calls', 'openInterest')
        self.dict_call_percent_change = self.create_dict_params_options('calls', 'percentChange')
        self.dict_call_contract_size = self.create_dict_params_options('calls', 'contractSize')
        self.dict_call_volume = self.create_dict_params_options('calls', 'volume')
        self.dict_call_currency = self.create_dict_params_options('calls', 'currency')
        self.dict_call_moneyness = self.create_dict_params_options('calls', 'inTheMoney')
        self.dict_call_change = self.create_dict_params_options('calls', 'change')
        self.dict_call_ask = self.create_dict_params_options('calls', 'ask')
        self.dict_call_bid = self.create_dict_params_options('calls', 'bid')
        self.dict_call_last_price = self.create_dict_params_options('calls', 'lastPrice')
        self.dict_call_last_trade_date = self.create_dict_params_options('calls', 'lastTradeDate')

    def create_df_individual_params_put(self):
        self.dict_put_implied_vol = self.create_dict_params_options('puts', 'impliedVolatility')
        self.dict_put_open_interest = self.create_dict_params_options('puts', 'openInterest')
        self.dict_put_percent_change = self.create_dict_params_options('puts', 'percentChange')
        self.dict_put_contract_size = self.create_dict_params_options('puts', 'contractSize')
        self.dict_put_volume = self.create_dict_params_options('puts', 'volume')
        self.dict_put_currency = self.create_dict_params_options('puts', 'currency')
        self.dict_put_moneyness = self.create_dict_params_options('puts', 'inTheMoney')
        self.dict_put_change = self.create_dict_params_options('puts', 'change')
        self.dict_put_ask = self.create_dict_params_options('puts', 'ask')
        self.dict_put_bid = self.create_dict_params_options('puts', 'bid')
        self.dict_put_last_price = self.create_dict_params_options('puts', 'lastPrice')
        self.dict_put_last_trade_date = self.create_dict_params_options('puts', 'lastTradeDate')

    def create_df_option(self):
        self.df_call_option = self.create_df_all_params(self.dict_calls)
        self.df_put_option = self.create_df_all_params(self.dict_calls)

    def dump_results(self):
        writer = pd.ExcelWriter(path_results + str(datetime.today()) + '.xlsx')
        self.df_call_option.to_excel(writer, 'call_options')
        self.df_put_option.to_excel(writer, 'put_options')
        writer.save()

    def create_df_all_params(self, dict_, list_params_options=list_params_options):
        temp_list_number_options = []
        for ticker in dict_.keys():
            for key in dict_[ticker].keys():
                temp_list_number_options.append(key)
        max_number_options = set(temp_list_number_options)
        list_index = self.create_list_params(list_params_options, self.list_ticker)
        temp_df = pd.DataFrame(data=0, index=list_index, columns=max_number_options)
        for ticker in dict_.keys():
            for option in dict_[ticker].keys():
                temp_loc_ = option
                for params in dict_[ticker][temp_loc_].keys():
                    temp_df.loc[ticker + ' ' + params, temp_loc_] = dict_[ticker][temp_loc_][params]
        return temp_df

    def create_dict_params_options(self, optionType, params):
        if optionType == 'calls':
            dict_option = self.dict_calls
        elif optionType == 'puts':
            dict_option = self.dict_puts
        dict_ = {}
        for ticker in dict_option.keys():
            temp_dict_ = {}
            i = 0
            for key in dict_option[ticker].keys():
                for key_ in dict_option[ticker][key].keys():
                    if key_ == params:
                        i += 1
                        try:
                            temp_dict_[i] = {params: dict_option[ticker][key][key_],
                                             'expirationDate': dict_option[ticker][key]['expiration'],
                                             'strike': dict_option[ticker][key]['strike']}
                        except Exception:
                            continue
                dict_[ticker] = temp_dict_
        return dict_

    @staticmethod
    def create_df_data(dict, list_ticker):
        temp_list_ = []
        for ticker in dict.keys():
            for key_ in dict[ticker].keys():
                temp_list_.append(key_)
        temp_list_ = set(temp_list_)
        temp_df = pd.DataFrame(data=0.0, index=temp_list_, columns=list_ticker)
        for ticker in dict.keys():
            for index in temp_df.index:
                try:
                    temp_df.loc[index, ticker] = dict[ticker][index]
                except:
                    temp_df.loc[index, ticker] = None
        return temp_df

    @staticmethod
    def create_dict_data_option(dict_results, option_type):
        dict_ = {}
        for ticker in dict_results.keys():
            i = 0
            for key in dict_results[ticker]['options'][0].keys():
                if key == option_type:
                    temp_dict_ = {}
                    for e_ in dict_results[ticker]['options'][0][key]:
                        i += 1
                        temp_dict_[i] = e_
                    dict_[ticker] = temp_dict_
        return dict_

    @staticmethod
    def create_list_params(list_params_options, list_ticker):
        temp_ = []
        for ticker in list_ticker:
            for param in list_params_options:
                temp_.append(ticker + ' ' + param)
        return temp_
