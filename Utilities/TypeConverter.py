from datetime import *

one_day_seconds = 86400
start_date_yahoo_api = datetime(1970, 1, 1)
start_int_yaho_api = 0

def convert_date_to_int_yahoo_api_format(date):
    laspe_ = date - start_date_yahoo_api
    int = (laspe_.total_seconds()) / 86400
    return int * one_day_seconds

def convert_int_to_date_yahoo_api_format(int):
    return start_date_yahoo_api + timedelta(seconds=int)

def remove_dec(int):
    int_ = str(int)
    int_.split('.')
    return int_[1]