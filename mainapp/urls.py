from django.urls import  path
from . import views


urlpatterns= [
    path('', views.index, name = 'index'),
    path('titan', views.titan, name = 'titan'),
    path('login', views.login, name = 'login'),
    path('signup', views.signUp, name = 'signUp'),
]