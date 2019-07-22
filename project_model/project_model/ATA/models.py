from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 100)
    no_telepon = models.SmallIntegerField()
    jabatan = models.CharField(max_length = 30)
    
class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 100)
    no_telepon = models.SmallIntegerField()
    nomor_absen = models.SmallIntegerField()
    nilai_rata_rata = models.FloatField()

class Mata_Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 50)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 100)
    no_telepon = models.SmallIntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 50)
    banyak_soal = models.SmallIntegerField()
    bobot_nilai = models.FloatField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 50)
    banyak_soal = models.SmallIntegerField()
    bobot_nilai = models.FloatField()
    tanggal_pelaksanaan = models.DateField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)
