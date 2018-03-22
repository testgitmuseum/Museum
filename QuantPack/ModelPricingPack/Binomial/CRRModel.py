from QuantPack.MathsTools.PricingPack.Binomial.BinomialTreeOption import BinomialTreeOption
import math


class CRRModel(BinomialTreeOption):

    def _setup_parameters_(self):
        self.u = math.exp(self.sigma * math.sqrt(self.dt))
        self.d = 1. / self.u
        self.qu = (math.exp((self.rate - self.dividend) * self.dt) - self.d) / (self.u - self.d)
        self.qd = 1 - self.qu
