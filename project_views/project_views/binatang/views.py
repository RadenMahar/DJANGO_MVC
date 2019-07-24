from django.shortcuts import render
from binatang.models import Binatang
from .form import InputBinatang

# Create your views here.
def daftar_binatang(request):
    binatang = Binatang.objects.all()
    return render(request, 'daftar_binatang.html', {'list_binatang':binatang})

def coba_html(request):
    return render(request, 'coba_html.html')

def input_binatang(request):
    if request.method == "POST":
        form = InputBinatang(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputBinatang()
    return render(request, 'daftar_binatang.html', {'form': form})

