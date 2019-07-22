from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.CharField(max_length = 50)
    bidang = models.CharField(max_length = 50)
    jadwal_praktek = models.DateField('Date')
    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.CharField(max_length = 50)
    alamat = models.TextField()
    keluhan = models.TextField()
    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length = 50)
    total_harga = models.CharField(max_length = 50)
    kumpulan_obat = models.TextField()
    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length = 50)
    kandungan = models.TextField()
    khasiat = models.TextField()
    def __str__(self):
        return self.nama