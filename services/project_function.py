from services.strategies import *

def project_function(periodReturns, periodFactRet, x0, short):
    Strategy = OLS_MVO()
    x = Strategy.execute_strategy(periodReturns, periodFactRet, short)
    return x
