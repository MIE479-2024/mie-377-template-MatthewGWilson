from services.strategies import *

def project_function(periodReturns, periodFactRet, x0, short, strategy, weights):
    if strategy == "OLS_MVO_ChatGPT":
        Strategy = OLS_MVO_ChatGPT()
        x = Strategy.execute_strategy(periodReturns, periodFactRet, short)
    elif strategy == "ChatGPT_Weights":
        Strategy = ChatGPT_Weights()
        x = Strategy.execute_strategy(weights)
    
    return x
