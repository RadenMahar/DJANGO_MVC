from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from ATA.models import Direksi, Mentee, Mentor, Mata_Pelajaran, Challenge, LiveCode
# Register your models here.

class DireksiDisplay(admin.ModelAdmin):
    list_display = ['id','nama_lengkap', 'no_telepon', 'jabatan']
    list_display_links = ['nama_lengkap']
    search_fields = ['nama_lengkap']
    list_filter = ['id', 'jabatan']

class MenteeDisplay(admin.ModelAdmin):
    list_display = ['id','nama_lengkap', 'no_telepon', 'nomor_absen', 'nilai_rata_rata']
    list_display_links = ['nama_lengkap']
    search_fields = ['nama_lengkap']
    list_filter = ['id','nama_lengkap', 'nomor_absen', 'nilai_rata_rata']

class MapelDisplay(admin.ModelAdmin):
    list_display = ['id','nama_pelajaran', 'jadwal_dimulai', 'jadwal_berakhir']
    list_display_links = ['nama_pelajaran']
    search_fields = ['nama_pelajaran']
    list_filter = ['id','nama_pelajaran']

class MentorDisplay(admin.ModelAdmin):
    list_display = ['id','nama_lengkap', 'no_telepon', 'mata_pelajaran']
    list_display_links = ['nama_lengkap']
    search_fields = ['nama_lengkap']
    list_filter = ['id','nama_lengkap', 'mata_pelajaran']

class ChallengeDisplay(admin.ModelAdmin):
    list_display = ['id','nama_challenge', 'banyak_soal', 'bobot_nilai', 'mata_pelajaran']
    list_display_links = ['nama_challenge']
    search_fields = ['nama_challenge']
    list_filter = ['id','nama_challenge', 'banyak_soal', 'mata_pelajaran']

class LCDisplay(admin.ModelAdmin):
    list_display = ['id','nama_live_code', 'banyak_soal', 'bobot_nilai','' 'mata_pelajaran']
    list_display_links = ['nama_live_code']
    search_fields = ['nama_live_code']
    list_filter = ['id','nama_live_code', 'banyak_soal', 'bobot_nilai', 'mata_pelajaran']

admin.site.register(Direksi, DireksiDisplay)
admin.site.register(Mentee, MenteeDisplay)
admin.site.register(Mentor, MentorDisplay)
admin.site.register(Mata_Pelajaran, MapelDisplay)
admin.site.register(Challenge, ChallengeDisplay)
admin.site.register(LiveCode, LCDisplay)
