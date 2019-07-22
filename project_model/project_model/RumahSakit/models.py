from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.IntegerField()
    bidang = models.CharField(max_length = 50)
    jadwal_praktek = models.DateField()

class Pasien(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.IntegerField()
    alamat = models.TextField()
    keluhan = models.TextField()

class Resep(models.Model):
    nama = models.CharField(max_length = 50)
    total_harga = models.FloatField()
    kumpulan_obat = models.TextField()

class Obat(models.Model):
    nama = models.CharField(max_length = 50)
    kandungan = models.TextField()
    khasiat = models.TextField()