from django.contrib import admin
from KebunBinatang.models import Hewan, Kandang, Penjaga, Pengunjung
# Register your models here.

admin.site.register(Hewan)
admin.site.register(Kandang)
admin.site.register(Penjaga)
admin.site.register(Pengunjung)

