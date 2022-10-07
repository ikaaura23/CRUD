from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Fakultas = models.CharField(max_length=200)
    Prodi = models.CharField(max_length=200)
    Alamatrumah = models.TextField(max_length=200)
    
    def __str__(self):
        return self.NIP

class Tendik(models.Model):
    NIP = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)
    Alamatrumah = models.TextField(max_length=200)
    def __str__(self):
        return self.NIP

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Fakultas = models.CharField(max_length=200)
    Prodi = models.TextField(max_length=200)

    def __str__(self):
        return self.NIM