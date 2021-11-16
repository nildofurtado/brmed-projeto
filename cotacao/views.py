from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post
from .serializers import CotacaoSerializer
from .controller.api import ConsultaApi
from .controller.consulta import ConsultaData

def index(request):
    d = ConsultaApi.index()
    esc = []
    for i in d:
        esc.append(
            {
            'id'        : i,
            'data_cotacao'      : d[i]['data'],
            'cotacao'   : {
                            'euro'  : d[i]['euro'],
                            'real'  : d[i]['real'],
                            'ien'   : d[i]['ien'],
                           }
            }
        )
    print(esc)    
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
            'data_cotacao'      : d[i]['data'],
            'cotacao'   : {
                            'euro'  : d[i]['euro'],
                            'real'  : d[i]['real'],
                            'ien'   : d[i]['ien'],
                           }
            }
        )
    return render(request, 'html/cotacao.html', {'retorno' : esc})
class CotacaoList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CotacaoSerializer