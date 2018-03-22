import math
import numpy as np

from QuantPack.MathsTools.PricingPack.Binomial.OptionBase import OptionBase


class BinomialTreeOption(OptionBase):

    def _setup_parameters_(self):
        self.u = 1 + self.pu
        self.d = 1 - self.pd
        self.qu = (math.exp((self.rate - self.dividend) * self.dt) - self.d) / (self.u - self.d)
        self.qd = 1 - self.qu

    def _initialize_stock_price_tree_(self):
        self.STs = [np.array([self.spot])]
        for i in range(self.n):
            prev_branches = self.STs[-1]
            st = np.concatenate((prev_branches * self.u, [prev_branches[-1] * self.d]))
            self.STs.append(st)

    def _initialize_payoffs_tree_(self):
        if self.is_call:
            return np.maximum(0, (self.STs[self.n]-self.strike))
        else:
            return self.strike - self.STs[self.n]

    def __check_early_exercise__(self, payoffs, node):
        if self.is_call:
            early_ex_payoff = (self.STs[node] - self.strike)
        else:
            early_ex_payoff = self.strike - self.STs[node]
        return np.maximum(payoffs, early_ex_payoff)

    def _traverse_tree_(self, payoffs):
        for i in reversed(range(self.n)):
            payoffs = (payoffs[:-1] * self.qu + payoffs[1:] * self.qd) * self.df
            if not self.is_european:
                payoffs = self.__check_early_exercise__(payoffs, i)
        return payoffs

    def __begin_tree_traversal__(self):
        payoffs = self._initialize_payoffs_tree_()
        return self._traverse_tree_(payoffs=payoffs)

    def price(self):
        self._setup_parameters_()
        self._initialize_stock_price_tree_()
        payoffs = self.__begin_tree_traversal__()
        return payoffs[0]
