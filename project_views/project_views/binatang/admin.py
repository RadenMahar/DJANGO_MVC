from django.contrib import admin
from binatang.models import Binatang
# Register your models here.

class BinatangDisplay(admin.ModelAdmin):
    list_display = ['nama', 'jenis']

admin.site.register(Binatang, BinatangDisplay)
