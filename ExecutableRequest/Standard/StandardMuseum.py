from datetime import timedelta
from Utilities.WebConnectDownload.MarketDataDownloader import *
from Utilities.GetParamsMuseumScript import *


class StandardMuseum:
    def __init__(self, module_path, global_path_utilities, compute_date, result_date):
        self.module_path = module_path
        self.compute_date = self.define_compute_date(compute_date)
        self.result_date = self.define_result_date(result_date, compute_date)
        self.global_path_utilities = global_path_utilities
        self.compute()

    def compute(self):
        self.list_tickers = get_tickers(self.global_path_utilities)
        self.list_source_data = get_source_data(self.global_path_utilities)
        self.run()

    def run(self):
        return None

    @staticmethod
    def define_compute_date(compute_date):
        if compute_date is None:
            return datetime.datetime.today()
        else:
            return compute_date

    @staticmethod
    def define_result_date(result_date, compute_date):
        if result_date is None:
            return compute_date - timedelta(days=1)
        else:
            return result_date


    # def backtest_date(self):
    #     if self.is_backtest is None:
    #         pass
