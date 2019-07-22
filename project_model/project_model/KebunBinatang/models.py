from django.db import models

# Create your models here.

class Hewan(models.Model):
    nama = models.CharField(max_length = 50)
    species = models.CharField(max_length = 50)
    berat = models.FloatField()
    umur = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length = 50)
    isi_kandang = models.TextField()
    luas_kandang = models.SmallIntegerField()
    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.CharField(max_length = 50)
    jadwal_jaga = models.DateTimeField('Date')
    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.CharField(max_length = 50)
    HARI_BERKUNJUNG = [
        ['Ming', 'Minggu'],
        ['Sen', 'Senin'],
        ['Sel', 'Selasa'],
        ['Rab', 'Rabu'],
        ['Kam', 'Kamis'],
        ['Jum', 'Jum\'at'],
        ['Sab', 'Sabtu'],
    ]
    hari_berkunjung = models.CharField(max_length = 10, choices = HARI_BERKUNJUNG, default = 'Ming')
    def __str__(self):
        return self.nama

