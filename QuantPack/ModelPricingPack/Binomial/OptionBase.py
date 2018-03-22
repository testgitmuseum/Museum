import math


class OptionBase(object):

    def __init__(self, spot, strike, rate, time, n, params):
        self.spot = spot
        self.strike = strike
        self.rate = rate
        self.time = time
        self.n = max(1, n)
        self.stockpricestree = None

        self.pu = params.get("pu", 0)
        self.pd = params.get("pd", 0)
        self.dividend = params.get("div", 0)
        self.sigma = params.get("sigma", 0)
        self.is_call = params.get("is_call", True)
        self.is_european = params.get("is_eu", True)
        self.dt = self.time / float(n)
        self.df = math.exp(-(self.rate - self.dividend) * self.dt)
