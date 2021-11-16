from .query import dbconsulta
import pandas as pd
import datetime
class ConsultaApi(object):
    def index():
        # gerando ranger de 5 dias contando pela data final. 
        df = pd.date_range(end=datetime.date.today(), periods=5)
        r = {}
        for i,j in enumerate(df):
            #consulta por uma class para melhoria de visualização da consulta e retorno.
            r[i] = dbconsulta.pesq_dupli_data(j.strftime("%Y-%m-%d"))
        return r

    def postCalendario(calendario):
        # gerando ranger de 5 dias contando pela data final. 
        r = {}
        esc = []
        for i,j in enumerate(calendario):
        #consulta por uma class para melhoria de visualização da consulta e retorno.
            r[i] = dbconsulta.pesq_dupli_data(j.strftime("%Y-%m-%d"))
        return r
       