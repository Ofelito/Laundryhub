# Generated by Django 4.1.7 on 2023-04-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pesanan_id_pes_alter_transaksi_id_tran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='Tgl_pes',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='Tgl_Tran',
            field=models.DateField(auto_now_add=True),
        ),
    ]
