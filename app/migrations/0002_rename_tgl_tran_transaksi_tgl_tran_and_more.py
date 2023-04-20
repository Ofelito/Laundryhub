# Generated by Django 4.1.7 on 2023-03-31 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaksi',
            old_name='tgl_Tran',
            new_name='Tgl_Tran',
        ),
        migrations.RemoveField(
            model_name='pesanan',
            name='Id_Tran',
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='Id_Pes',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='Id_Pes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pesanan'),
        ),
    ]