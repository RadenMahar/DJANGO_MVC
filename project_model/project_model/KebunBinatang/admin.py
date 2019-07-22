from django.contrib import admin
from KebunBinatang.models import Hewan, Kandang, Penjaga, Pengunjung
# Register your models here.

class HewanDisplay(admin.ModelAdmin):
    list_display = ['id', 'nama', 'species', 'berat', 'umur']
    list_display_links = ['nama']
    search_fields = ['nama', 'species']

class KandangDisplay(admin.ModelAdmin):
    list_display = ['id', 'nama', 'isi_kandang', 'luas_kandang']
    list_display_links = ['nama']
    search_fields = ['nama']

class PenjagaDisplay(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'jadwal_jaga']
    list_display_links = ['nama']
    search_fields = ['nama']

class PengunjungDisplay(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'hari_berkunjung']
    list_display_links = ['nama']
    search_fields = ['nama']

admin.site.register(Hewan, HewanDisplay)
admin.site.register(Kandang, KandangDisplay)
admin.site.register(Penjaga, PenjagaDisplay)
admin.site.register(Pengunjung, PengunjungDisplay)

