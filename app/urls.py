from django.urls import path
from .views import index,Login,pesanan,postpelanggan,history,details,v_transaksi,posttransaksi

urlpatterns =[
    path('Login/', Login, name='Login'),
    path('index', index,name='index'),              
    path('pesanan', pesanan,name='pesanan'),       
    path('postpelanggan', postpelanggan,name='postpelanggan'),      
    path('posttransaksi', posttransaksi,name='posttransaksi'),      
    path('Transaksi', v_transaksi,name='Transaksi'),       
    path('historiy', history,name='history'),       
    path('details', details,name='details'),       
]