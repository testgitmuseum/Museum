dict_url = {}
dict_object = {}
dict_results = {}
dict_quote = {}
dict_calls = {}
dict_puts = {}
dict_call_implied_vol = {}
dict_call_open_interest= {}
dict_call_percent_change= {}
dict_call_contract_size= {}
dict_call_volume= {}
dict_call_currency= {}
dict_call_moneyness= {}
dict_call_change= {}
dict_call_ask= {}
dict_call_bid= {}
dict_call_last_price= {}
dict_call_last_trade_date= {}
dict_put_implied_vol= {}
dict_put_open_interest= {}
dict_put_percent_change= {}
dict_put_contract_size= {}
dict_put_volume= {}
dict_put_currency= {}
dict_put_moneyness= {}
dict_put_change= {}
dict_put_ask= {}
dict_put_bid= {}
dict_put_last_price= {}
dict_put_last_trade_date= {}

list_ticker = ['^GSPC', 'AMZN']
global_path = r'https://query2.finance.yahoo.com/v7/finance/options/'
for ticker in list_ticker:
    dict_url[ticker] = global_path + ticker
for ticker in dict_url.keys():
    temp_ = urllib2.urlopen(dict_url[ticker])
    dict_object[ticker] = json.load(temp_)
for ticker in dict_object.keys():
    dict_results[ticker] = dict_object[ticker]['optionChain']['result'][0]
for ticker in dict_results.keys():
    for key in dict_results[ticker].keys():
        if key == 'quote':
            temp_dict_ = {}
            for key_ in dict_results[ticker][key].keys():
                temp_dict_[key_] = dict_results[ticker][key][key_]
            dict_quote[ticker] = temp_dict_

def create_df_data(dict_quote, list_ticker):
    temp_list_ = []
    for ticker in dict_quote.keys():
        for key_ in dict_quote[ticker].keys():
            temp_list_.append(key_)
    temp_list_ = set(temp_list_)
    temp_df = pd.DataFrame(data=0.0, index=temp_list_, columns=list_ticker)
    for ticker in dict_quote.keys():
        for index in temp_df.index:
            try:
                temp_df.loc[index, ticker] = dict_quote[ticker][index]
            except:
                temp_df.loc[index, ticker] = None
    return temp_df

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

dict_calls = create_dict_data_option(dict_results, 'calls')
dict_puts = create_dict_data_option(dict_results, 'puts')


def create_dict_params_options(optionType, params):
    if optionType == 'calls':
        dict = dict_calls
    elif optionType == 'puts':
        dict = dict_puts
    dict_ = {}
    for ticker in dict.keys():
        temp_dict_ = {}
        i = 0
        for key in dict[ticker].keys():
            for key_ in dict[ticker][key].keys():
                if key_ == params:
                    i += 1
                    try:
                        temp_dict_[i] = {params: dict[ticker][key][key_],
                                         'expirationDate': dict[ticker][key]['expiration'],
                                         'strike': dict[ticker][key]['strike']}
                    except Exception:
                        continue
            dict_[ticker] = temp_dict_
    return dict_

dict_call_implied_vol = create_dict_params_options('calls', 'impliedVolatility')
dict_call_open_interest = create_dict_params_options('calls', 'openInterest')
dict_call_percent_change = create_dict_params_options('calls', 'percentChange')
dict_call_contract_size = create_dict_params_options('calls', 'contractSize')
dict_call_volume = create_dict_params_options('calls', 'volume')
dict_call_currency = create_dict_params_options('calls', 'currency')
dict_call_moneyness = create_dict_params_options('calls', 'inTheMoney')
dict_call_change = create_dict_params_options('calls', 'change')
dict_call_ask = create_dict_params_options('calls', 'ask')
dict_call_bid = create_dict_params_options('calls', 'bid')
dict_call_last_price = create_dict_params_options('calls', 'lastPrice')
dict_call_last_trade_date = create_dict_params_options('calls', 'lastTradeDate')
dict_put_implied_vol = create_dict_params_options('puts', 'impliedVolatility')
dict_put_open_interest = create_dict_params_options('puts', 'openInterest')
dict_put_percent_change = create_dict_params_options('puts', 'percentChange')
dict_put_contract_size = create_dict_params_options('puts', 'contractSize')
dict_put_volume = create_dict_params_options('puts', 'volume')
dict_put_currency = create_dict_params_options('puts', 'currency')
dict_put_moneyness = create_dict_params_options('puts', 'inTheMoney')
dict_put_change = create_dict_params_options('puts', 'change')
dict_put_ask = create_dict_params_options('puts', 'ask')
dict_put_bid = create_dict_params_options('puts', 'bid')
dict_put_last_price = create_dict_params_options('puts', 'lastPrice')
dict_put_last_trade_date = create_dict_params_options('puts', 'lastTradeDate')

list_params_options = ['impliedVolatility', 'openInterest', 'percentChange', 'contractSize', 'volume', 'currency',
                       'inTheMoney', 'change', 'ask', 'bid', 'lastPrice', 'lastTradeDate']
def create_list_params(list_params_options, list_ticker):
    temp_ = []
    for ticker in list_ticker:
        for param in list_params_options:
            temp_.append(ticker + ' ' + param)
    return temp_


temp_list_number_options = []
for ticker in dict_calls.keys():
    temp_list_number_options = []
    for key in dict_calls[ticker].keys():
        temp_list_number_options.append(key)
max_number_options = set(temp_list_number_options)
list_index = create_list_params(list_params_options, list_ticker)
df = pd.DataFrame(data=0, index=list_index, columns=max_number_options)

for ticker in dict_calls.keys():
    for option in dict_calls[ticker].keys():
        temp_loc_ = option
        for params in dict_calls[ticker][temp_loc_].keys():
            df.loc[ticker + ' ' + params, temp_loc_] = dict_calls[ticker][temp_loc_][params]




