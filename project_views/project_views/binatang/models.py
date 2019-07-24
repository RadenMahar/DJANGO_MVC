from django.db import models

# Create your models here.
class Binatang(models.Model):
    nama = models.CharField(max_length = 50)
    jenis = models.CharField(max_length = 50)
    umur = models.IntegerField()
    def __str__(self):
        return self.nama
