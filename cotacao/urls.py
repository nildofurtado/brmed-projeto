from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'cotacao'
urlpatterns = [
    path('', views.index, name='index'),
    path('consulta/', views.consulta, name='consulta'),
    url(r'^api/$', views.CotacaoList.as_view(), name='cotacao-list'),
]
