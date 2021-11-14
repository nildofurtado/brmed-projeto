import pandas as pd

class ConsultaData():
    def periodo(datai,dataf):
        if(datai == ''):
            periodo = pd.date_range(end=dataf, periods=5)
            return periodo
        
        elif(datai == dataf): 
            periodo = pd.date_range(end=dataf, periods=5)
            return periodo
        
        elif(datai > dataf):
            periodo = pd.date_range(end=dataf, periods=5)
            return periodo
        
        elif(datai < dataf):
            periodo = pd.date_range(end=dataf, periods=5)
            return periodo
        
        else:
            periodo = pd.date_range(start=datai, end=dataf, periods=5)
            return periodo