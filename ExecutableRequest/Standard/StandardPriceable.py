from ExecutableRequest.StandardMuseum import StandardMuseum
from Utilities.GetParamsMuseumScript import *
import pandas as pd

__author__ = 'vfourrier'


class StandardPriceable(StandardMuseum):
    def __init__(self, module_path, global_path_utilities, compute_date, result_date):
        StandardMuseum.__init__(self, module_path, global_path_utilities, compute_date, result_date)
        self.dict_params = StandardPriceable.get_eqd_options_params(self)

    def create_params(self):
        self.df_params = self.dict_params['df_params']
        self.number_option = self.dict_params['number_options']
        self.list_params = self.dict_params['list_params']
        self.list_asset_class = set(self.dict_params['list_asset_class'])

    def get_eqd_options_params(self):
        return get_equity_options_params(self.global_path_utilities)

    def get_ir_swaps_params(self):
        return get_equity_options_params(self.global_path_utilities)

    def get_ird_options_params(self):
        return get_equity_options_params(self.global_path_utilities)

    def get_fx_options_params(self):
        return get_equity_options_params(self.global_path_utilities)

    def get_commodity_options_params(self):
        return get_equity_options_params(self.global_path_utilities)

    def get_fx_swaps_params(self):
        return get_equity_options_params(self.global_path_utilities)






