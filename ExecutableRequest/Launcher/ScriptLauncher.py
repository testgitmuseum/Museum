from datetime import datetime
from datetime import timedelta
import importlib
import sys

__author__ = 'vfourrier'


def run(module_path, global_path_utilities, compute_date, result_date):
    module_launcher = module_path
    class_module = module_path.split('.')[-1]
    importlib.import_module(module_launcher)
    run_module = sys.modules[module_launcher]
    run_class = getattr(run_module, class_module)
    run_class(module_path=module_path + class_module, global_path_utilities=global_path_utilities, compute_date=compute_date,
              result_date=result_date)


def main():
    module_path = 'QuantPack.Equity.Products.Options.EQDPriceable'
    compute_date = datetime(2018, 1, 1)
    result_date = compute_date - timedelta(days=1)
    global_path_utilities = r'/Volumes/SECURITY 1/Vincent/BSCM/ATM/Utilities/GetParams/Museum_Wrapper.xlsx'

    run(module_path=module_path, global_path_utilities=global_path_utilities, compute_date=compute_date,
        result_date=result_date)


if __name__ == '__main__':
    main()

