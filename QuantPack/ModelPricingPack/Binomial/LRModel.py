from QuantPack.MathsTools.PricingPack.Binomial.BinomialTreeOption import BinomialTreeOption
import math


class LRModel(BinomialTreeOption):

    def _setup_parameters_(self):
        odd_n = self.n if (self.n % 2 == 1) else (self.n + 1)
        d1 = (math.log(self.spot / self.strike) +
              ((self.rate - self.dividend) +
               (self.sigma ** 2) / 2.) *
              self.time) / (self.sigma * math.sqrt(self.time))
        d2 = (math.log(self.spot / self.strike) +
              ((self.rate - self.dividend) -
               (self.sigma ** 2) / 2.) *
              self.time) / (self.sigma * math.sqrt(self.time))
        pp_2_inversion = lambda z, n: .5 + math.copysign(1, z) * math.sqrt(.25 - .25 *
                                                                           math.exp(-((z / (n + 1. / 3. + .1 /
                                                                                    (n + 1))) ** 2.) *
                                                                                    (n + 1. / 6.)))
        p_bar = pp_2_inversion(d1, odd_n)
        self.p = pp_2_inversion(d2, odd_n)
        self.u = 1 / self.df * p_bar / self.p
        self.d = (1 / self.df - self.p * self.u) / (1 - self.p)
        self.qu = self.p
        self.qd = 1 - self.p

