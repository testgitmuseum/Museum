import pandas as pd


def get_tickers(global_path_utilities):
    temp_df = pd.read_excel(global_path_utilities, sheet_name='Tickers')
    df = temp_df.set_index('Params')
    list_tickers = df.loc['list_tickers', 'Results'].split(';')
    return list_tickers


def get_source_data(global_path_utilities):
    temp_df = pd.read_excel(global_path_utilities, sheet_name='Tickers')
    df = temp_df.set_index('Params')
    list_source_data = df.loc['source_data', 'Results'].split(';')
    return list_source_data


def get_equity_options_params(global_path_utilities):
    temp_df = pd.read_excel(global_path_utilities, sheet_name='Equity_Options')
    df_equity_options_wrapper = temp_df.set_index('Option Number')
    list_params = list(df_equity_options_wrapper)
    number_option = get_number_option_to_price(df_equity_options_wrapper)
    list_asset_class = get_asset_class(df_equity_options_wrapper)
    dict_ = {'df_params': df_equity_options_wrapper, 'list_params': list_params,
             'number_options': number_option, 'list_asset_class': list_asset_class}
    return dict_


def get_number_option_to_price(df_equity_options_wrapper):
    temp_ = 0.0
    for index in df_equity_options_wrapper.index:
        if df_equity_options_wrapper.loc[index, 'To_Price'] == 'YES':
            temp_ += 1
    return temp_


def get_asset_class(df_equity_options_wrapper):
    temp_list_ = []
    for index in df_equity_options_wrapper.index:
        temp_list_.append(df_equity_options_wrapper.loc[index, 'Asset_Category'])
    return temp_list_

