from django.urls import path
from .views import index,Login

urlpatterns =[
    path('Login/', Login, name='Login'),
    path('index', index,name='index'),
]

