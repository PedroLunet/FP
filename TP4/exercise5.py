def deriv(f):
    def df(x):
        h = 0.001 
        dfx = (f(x + h) - f(x)) / h  
        return round(dfx, 3)  
    return df