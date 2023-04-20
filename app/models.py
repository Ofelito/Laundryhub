from django.db import models

# Create your models here.
class Admin(models.Model):
    Id_Adm = models.CharField(max_length=4, primary_key=True)
    Nama = models.CharField(max_length=20)
    Status = models.CharField(max_length=10)
    Password = models.CharField(max_length=12)

class Pelanggan(models.Model):
    Id_Pel = models.CharField(max_length=12, primary_key=True)
    Nama = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Alamat = models.CharField(max_length=120)

class Pesanan(models.Model):
    Id_Pes = models.CharField(max_length=12,primary_key=True)
    Jumlah = models.IntegerField()
    Tgl_pes = models.CharField(max_length=20)
    Id_ADM = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Id_Pel = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)

class Transaksi(models.Model):
    Id_Tran = models.CharField(max_length=12,primary_key=True)
    Tgl_Tran = models.CharField(max_length=20)
    Jumlah_Uang = models.IntegerField()
    Kembalian = models.IntegerField(null = True)
    Id_Pes = models.ForeignKey(Pesanan, on_delete=models.CASCADE)



