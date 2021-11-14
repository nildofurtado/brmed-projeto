from django.urls import path
from . import views
app_name = 'cotacao'
urlpatterns = [
    path('', views.index, name='index'),
    path('consulta/', views.consulta, name='consulta'),
]
