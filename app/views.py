from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Admin, Pelanggan, Transaksi, Pesanan
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

def post_barang(request):
    Nama = request.POST['Nama']
    Jumlah = request.POST['Jumlah']
    if Barang.objects.filter(kodebarang=kodebarang).exists():
        messages.error(request, 'Kode Barang Sudah Di Gunakan !!')
        return redirect(request.META.get('HTTP_REFERER','/'))
    else :
        Tambah_Barang = Barang(
            kodebarang=kodebarang,
            namabarang=namabarang
        )
        Tambah_Barang.save()
        messages.success(request, 'Data Berhasil Di Tambahkan')
    return redirect('masterbarang')