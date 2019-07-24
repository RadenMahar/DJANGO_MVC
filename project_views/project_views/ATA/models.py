from django.db import models

# Create your models here.
class Mentee(models.Model):
    nama = models.CharField(max_length = 50)
    picture = models.CharField(max_length = 255)
    moto = models.TextField()

class Mentor(models.Model):
    nama = models.CharField(max_length = 50)
    jobStatus = models.CharField(max_length = 255)
    moto = models.TextField()
    picture = models.CharField(max_length = 255)

class Blog(models.Model):
    picture = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    head = models.CharField(max_length = 255)
    text = models.TextField()
