# Generated by Django 4.1.7 on 2023-04-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_tgl_tran_transaksi_tgl_tran_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='Id_Pes',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='Id_Tran',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]