from django.contrib import admin
from RumahSakit.models import Dokter, Pasien, Resep, Obat
# Register your models here.

class DokterDisplay(admin.ModelAdmin):
    list_display = ['id','nama', 'nomor_telepon', 'bidang']
    list_display_links = ['nama', 'bidang']
    search_fields = ['nama']

class PasienDisplay(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'alamat']
    list_display_links = ['nama']
    search_fields = ['nama', 'nomor_telepon']

class ResepDisplay(admin.ModelAdmin):
    list_display = ['id','nama', 'total_harga', 'kumpulan_obat']
    list_display_links = ['nama']
    search_fields = ['nama']

class ObatDisplay(admin.ModelAdmin):
    list_display = ['id','nama', 'kandungan', 'khasiat']
    list_display_links = ['nama']
    search_fields = ['nama', 'kandungan']

admin.site.register(Dokter, DokterDisplay)
admin.site.register(Pasien, PasienDisplay)
admin.site.register(Resep, ResepDisplay)
admin.site.register(Obat, ObatDisplay)

