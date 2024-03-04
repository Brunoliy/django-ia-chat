from django.urls import path
from langchat import views


urlpatterns = [
    path('', views.index, name='index'),
    path('getResponse', views.getResponse, name='getResponse')

]