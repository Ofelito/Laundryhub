from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime,date
from .Utilities import hitung_kilo,hitung_kembalian,tambah_nol
from .models import Admin, Pelanggan, Transaksi, Pesanan
import json
# Create your views here.



def Login(request):
    if request.method == 'POST':
        Id_Adm = request.POST.get('Admin')
        Password = request.POST.get('Password')
        if Admin.objects.filter(Id_Adm=Id_Adm ).exists():
            admin = Admin.objects.get(Id_Adm=Id_Adm)
            if admin.Password == Password:
                request.session['idadmin'] = admin.Id_Adm
                request.session['nmadmin'] = admin.Nama
                request.session['stsadmin'] = admin.Status
                request.session.save()
                return redirect('index')
            else:
                # Return an error message if the login credentials are invalid
                error_message = 'Invalid login credentials. Please try again.'
        else:
            # Return an error message if the login credentials are invalid
            error_message = 'Invalid login credentials. Please try again.'
    return render(request, 'Login.html')

def index(request):
    return render(request, 'index.html/')

def postpelanggan(request):
    if request.method == 'POST':
        my_date= date.today()
        formatted_date = my_date.strftime('%y-%m-%d')
        # pelanggan
        if Pelanggan.objects.all().exists() :
            cek_pelanggan = Pelanggan.objects.all().order_by('-Id_Pel').first()
            last_Id_Pel = cek_pelanggan.Id_Pel[10:12]
            nomorurut = str(int(last_Id_Pel)+1)
            if(len(nomorurut) < 2):
                nomorurut = tambah_nol(nomorurut,2)
        else : 
            nomorurut = '01'
        Id_Pel= 'P'+str(formatted_date)+'l'+nomorurut
        # pesananan
        if Pesanan.objects.all().exists() :
            cek_pesanan = Pesanan.objects.all().order_by('-Id_Pes').first()
            last_Id_Pes = cek_pesanan.Id_Pes[10:12]
            nomorurut = str(int(last_Id_Pes)+1)
            if(len(nomorurut) < 2):
                nomorurut = tambah_nol(nomorurut,2)
        else : 
            nomorurut = '01'
        Id_Pes= 'P'+str(formatted_date)+'s'+nomorurut
        # return HttpResponse(Id_Pel)
        Nama = request.POST['Nama']
        Kg = request.POST['Kg']
        hasil = hitung_kilo(Kg)
        now = datetime.now()
        Tanggal = now.strftime("%Y-%m-%d")
        Email = request.POST['Email']
        Alamat = request.POST['Alamat']
        Id_Adm =request.session['idadmin']
        Tambah_Pelanggan = Pelanggan(
            Id_Pel=Id_Pel,
            Nama=Nama,
            Email=Email,
            Alamat=Alamat
        )
        Tambah_Pelanggan.save()
        Tambah_Pesanan = Pesanan(
            Id_Pes=Id_Pes,
            Jumlah=hasil,
            Tgl_pes=Tanggal,
            Id_ADM_id=Id_Adm,
            Id_Pel_id=Id_Pel
        )
        Tambah_Pesanan.save()
        pesanan = Pesanan.objects.get(Id_Pes=Id_Pes)
        request.session['idpes'] = pesanan.Id_Pes
        request.session['jmlh'] = pesanan.Jumlah
        request.session['tglpes'] = pesanan.Tgl_pes
        request.session.save()
        pelanggan = Pelanggan.objects.get(Id_Pel=Id_Pel)
        request.session['idpel'] = pelanggan.Id_Pel
        request.session['nmpelanggan'] = pelanggan.Nama
        request.session['email'] = pelanggan.Email
        request.session['almt'] = pelanggan.Alamat
        request.session.save()
    return redirect('pesanan')

def pesanan(request):
    return render(request, 'pesanan.html')

def posttransaksi(request):
    if request.method == 'POST':
        my_date= date.today()
        formatted_date = my_date.strftime('%y-%m-%d')
        # Transaksi
        if Transaksi.objects.all().exists() :
            cek_transaksi = Transaksi.objects.all().order_by('-Id_Tran').first()
            last_Id_Tran = cek_transaksi.Id_Tran[10:12]
            nomorurut = str(int(last_Id_Tran)+1)
            if(len(nomorurut) < 2):
                nomorurut = tambah_nol(nomorurut,2)
        else : 
            nomorurut = '01'
        Id_Tran= 'T'+str(formatted_date)+'r'+nomorurut
        # return HttpResponse(Id_Tran)
        Id_Pes= request.session['idpes']
        total = request.session['jmlh']
        jmlh_uang = request.POST['jmlh_uang']
        Kembalian = hitung_kembalian(jmlh_uang,total)
        now = datetime.now()
        Tanggal = now.strftime("%Y-%m-%d")
        Tambah_Transaksi = Transaksi(
            Id_Tran=Id_Tran,
            Tgl_Tran=Tanggal,
            Jumlah_Uang=total,
            Id_Pes_id=Id_Pes,
            Kembalian=Kembalian
        )
        Tambah_Transaksi.save()
        transaksi = Transaksi.objects.get(Id_Tran=Id_Tran)
        request.session['kmbl'] = transaksi.Kembalian
        request.session.save()
    return redirect('Transaksi')

def v_transaksi(request):
    return render(request, 'transaksi.html')

def history(request):
    data_transaksi = Transaksi.objects.all()
    # data_pesanan = Pesanan.objects.all()
    context = {
        'data_transaksi' : data_transaksi
        # 'data_pesanan' : data_pesanan
    }
    return render(request,'history.html',context)

def details(request):
    data_transaksi = Transaksi.objects.all()
    context = {
        'data_transaksi' : data_transaksi
    }
    return render(request,'details.html',context)