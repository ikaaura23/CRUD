# Generated by Django 4.1 on 2022-10-05 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIM', models.CharField(max_length=50)),
                ('Nama', models.CharField(max_length=40)),
                ('TanggalLahir', models.CharField(max_length=40)),
                ('Photo', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('Fakultas', models.CharField(max_length=40)),
                ('Prodi', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=50)),
                ('Nama', models.CharField(max_length=40)),
                ('TanggalLahir', models.CharField(max_length=40)),
                ('Photo', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('Unit', models.CharField(max_length=40)),
                ('Alamatrumah', models.TextField(max_length=40)),
            ],
        ),
    ]
