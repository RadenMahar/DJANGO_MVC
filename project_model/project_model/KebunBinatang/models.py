from django.db import models

# Create your models here.

class Hewan(models.Model):
    nama = models.CharField(max_length = 50)
    species = models.CharField(max_length = 50)
    berat = models.FloatField()
    umur = models.PositiveSmallIntegerField()

class Kandang(models.Model):
    nama = models.CharField(max_length = 50)
    isi_kandang = models.TextField()
    luas_kandang = models.SmallIntegerField()

class Penjaga(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.SmallIntegerField()
    jadwal_jaga = models.DateTimeField('Date')

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.SmallIntegerField()
    hari_berkunjung = models.DateField()


