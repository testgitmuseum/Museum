from Utilities import ParamsObject

class HestonVolatility(ParamsObject):
    def __init__(self):

    def run(self):
        return None

    def evaluate_heston_vol(self):
        self.take_data()
        self.calibrate_interest_rate_model()

    def take_data(self):
        lib = ParamsObject()

    def calibrate_interest_rate_model(self):
