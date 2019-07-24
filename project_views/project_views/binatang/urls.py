from django.urls import path
from . import views

urlpatterns = [
    # name untuk alias
    path('hewan/', views.daftar_binatang, name = 'daftar_binatang'),
    path('coba/', views.coba_html, name = 'coba'),
    path('input/', views.input_binatang, name = 'input')
]