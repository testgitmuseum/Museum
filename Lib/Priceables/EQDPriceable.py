from ExecutableRequest.StandardPriceable import StandardPriceable
from Utilities.WebConnectDownload.MarketDataDownloader import *


class EQDPriceable(StandardPriceable):
    def __init__(self, module_path, global_path_utilities, compute_date, result_date):
        StandardPriceable.__init__(self, module_path, global_path_utilities, compute_date, result_date)
        self.eqd_priceable = {}
        self.list_underlyings = []
        self.dict_df_spot_price = {}
        self.pricing_params = {}

    def run(self):
        self.dict_params = StandardPriceable.get_eqd_options_params(self)
        StandardPriceable.create_params(self)
        if len(self.list_asset_class) == 1 and 'equity' in self.list_asset_class:
            self.one_underlying_priceable()

    def one_underlying_priceable(self):
        self.eqd_priceable = self.get_eqd_priceable()
        self.pricing_params = self.get_underlyings()
        self.get_underlying_data()
        # self.get_volatility()
        # self.get_interest_rates()
        # self.get_fx_quanto()
        # self.get_strike()
        # self.get_pricing_method()

    def get_underlyings(self):
        temp_dict_ = {}
        for key_ in self.eqd_priceable.keys():
            temp_dict_[key_] = {'Underlying_Asset': self.eqd_priceable[key_]['Underlying_Asset'],
                          'Trade_Date': self.eqd_priceable[key_]['Trade_Date'],
                          'Maturity_Date': self.eqd_priceable[key_]['Maturity_Date'],
                          'Strike_Date': self.eqd_priceable[key_]['Strike_Date']}
        return temp_dict_

    def get_underlying_data(self):
        if self.list_source_data == 'web':
            downloader = MarketDataDownloader(self.list_tickers, self.compute_date, self.result_date)
            for key_ in self.pricing_params.keys():
                und_ = self.pricing_params[key_]['Underlying_Asset']
                spot = self.pricing_params[key_]['Strike_Date']
                df_ = downloader.get_stock_data()
                self.pricing_params[key_]['Close_Price'] = df_.loc[spot, 'Close']
                self.pricing_params[key_]['Open_Price'] = df_.loc[spot, 'Open']
                self.pricing_params[key_]['High_Price'] = df_.loc[spot, 'High']
                self.pricing_params[key_]['Low_Price'] = df_.loc[spot, 'Low']
                self.pricing_params[key_]['Adj_Price'] = df_.loc[spot, 'Adj Close']
                self.pricing_params[key_]['Volume'] = df_.loc[spot, 'Volume']
                # df_ = None
                # df_ = downloader.get_dividend_ost_value(und_, start_downloading_date=spot, end_downloading_date=spot)
                # df_ = None
                # df_ = downloader.get_historical_dividend(und_, start_downloading_date=spot, end_downloading_date=spot)
        elif self.list_source_data == 'csv':
            return None
        elif self.list_source_data == 'excel':
            return None
        elif self.list_source_data == 'screen_data':
            """ our api """
            return None

    # def get_volatility(self):
    #     for key_ in self.eqd_priceable.keys():
    #         temp_ = self.eqd_priceable[key_]['Option_Sigma_Type']
    #         _temp = self.eqd_priceable[key_]['Option_Sigma_Method']
    #         _temp_ = self.eqd_priceable[key_]['Option_Sigma']
    #         self.pricing_params[key_]['Option_Sigma_Type'] = temp_
    #         self.pricing_params[key_]['Option_Sigma_Method'] = _temp
    #         self.pricing_params[key_]['Option_Sigma'] = _temp_
    #     for key_ in self.eqd_priceable.keys():
    #         if self.pricing_params[key_]['Option_Sigma_Type'] == 'Compute':
    #             temp_ = self.pricing_params[key_]['Option_Sigma_Method']
    #             if isnan(temp_):
    #                 break
    #             else:
    #                 if temp_ == 'Dupire':
    #                     vol = Dupire()
    #                     self.pricing_params[key_]['Option_Sigma'] = vol.run()
    #                 elif temp_ == 'Heston':
    #                     vol = HestonVolatility()
    #                     self.pricing_params[key_]['Option_Sigma'] = vol.run()
    #                 elif temp_ == 'Implied_Vol':
    #                     vol = ImpliedVol()
    #                     self.pricing_params[key_]['Option_Sigma'] = vol.run()
    #         try:
    #             isnan(self.pricing_params[key_]['Option_Sigma_Type'])
    #             sys.exit(0)
    #         except:
    #             self.pricing_params[key_]['Option_Sigma_Type'] = self.pricing_params[key_]['Option_Sigma_Type']

    def get_eqd_priceable(self):
        temp_dict_ = {}
        temp_ = {}
        for index in self.df_params.index[:self.number_option]:
            if index <= self.number_option:
                for e_ in self.list_params:
                    key_ = e_
                    temp_[key_] = self.df_params.loc[index, key_]
            temp_dict_[index] = temp_
        return temp_dict_













