# Generated by Django 4.1 on 2022-10-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0002_mahasiswa_tendik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='Alamatrumah',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Fakultas',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='NIP',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Nama',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Photo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='Prodi',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dosen',
            name='TanggalLahir',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='Email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='Fakultas',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='NIM',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='Nama',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='Photo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='Prodi',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='TanggalLahir',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='Alamatrumah',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='Email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='NIP',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='Nama',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='Photo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='TanggalLahir',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tendik',
            name='Unit',
            field=models.CharField(max_length=200),
        ),
    ]
