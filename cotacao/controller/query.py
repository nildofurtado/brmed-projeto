from ..models import Post
import requests

class dbconsulta():
    #verifica se já existe data cadastrada no dia
    def pesq_dupli_data(dt):
        d = Post.objects.all().filter(dt_vl=dt)
        r = {}
        if len(d) == 0:
            rgravar = dbconsulta.gravar_consulta(dt)
            r = {
                'Status' : rgravar
            }
        else:
            for i in d:
                r = {
                        'data'  : i.dt_vl,
                        'real'  : i.vl_brl,
                        'euro'  : i.vl_eur,
                        'ien'   : i.vl_ien,
                    }
        return r

    def gravar_consulta(dt):
        url = 'https://api.vatcomply.com/rates?base=USD&symbols=JPY,EUR,BRL&date=' + dt
        req = requests.get(url)
        row = req.json()
        reg_row = Post(logIp='0.0.0.0', dt_vl=dt, vl_brl=row['rates']['BRL'], vl_ien=row['rates']['JPY'], vl_eur=row['rates']['EUR'])
        reg_row.save()
        
        
    def select_cotacao(dt):
        d = Post.objects.all().filter(dt_vl=dt)
        r = {}
        for i in d:
            r = [{
                'data' : i.dt_vl,
                'real' : i.vl_brl,
                'euro' : i.vl_eur,
                'ien' : i.vl_ien,
            }]
        return r 