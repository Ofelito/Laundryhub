# Generated by Django 4.1.7 on 2023-04-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_pesanan_tgl_pes_alter_transaksi_tgl_tran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='Tgl_pes',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='Tgl_Tran',
            field=models.DateField(),
        ),
    ]
