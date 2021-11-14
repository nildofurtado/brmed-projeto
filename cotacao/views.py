from django.shortcuts import render
from .controller.api import ConsultaApi
from .controller.consulta import ConsultaData
from django.shortcuts import redirect

def index(request):
    d = ConsultaApi.index()
    esc = []
    for i in d:
        esc.append(
            {
            'id'        : i,
            'data'      : d[i]['data'],
            'cotacao'   : {
                            'euro'  : d[i]['euro'],
                            'real'  : d[i]['real'],
                            'ien'   : d[i]['ien'],
                           }
            }
        )
    return render(request, 'html/cotacao.html', {'retorno' : esc})

def consulta(request):
    if(request.method == 'GET'):
        return redirect('/')
    else:   
        esc = [] 
        dtinicial   =  request.POST['datei']
        dtfinal     =  request.POST['datef']
        
        DataRetorno = ConsultaData.periodo(dtinicial,dtfinal)
        d = ConsultaApi.postCalendario(DataRetorno)
        for i in d:
            esc.append(
                {
                'id'        : i,
                'data'      : d[i]['data'],
                'cotacao'   : {
                                'euro'  : d[i]['euro'],
                                'real'  : d[i]['real'],
                                'ien'   : d[i]['ien'],
                               }
                }
            )
    return render(request, 'html/cotacao.html', {'retorno' : esc})