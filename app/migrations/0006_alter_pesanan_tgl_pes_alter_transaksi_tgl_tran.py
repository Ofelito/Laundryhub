# Generated by Django 4.1.7 on 2023-04-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_pesanan_tgl_pes_alter_transaksi_tgl_tran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='Tgl_pes',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='Tgl_Tran',
            field=models.CharField(max_length=20),
        ),
    ]