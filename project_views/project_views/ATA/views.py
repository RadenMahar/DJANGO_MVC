from django.shortcuts import render
from .models import Mentor, Mentee, Blog
from .form import InputMentor, InputMentee, InputBlog


# Create your views here.
def HalamanHome(request):
    return render(request, 'Home.html')
def HalamanBlog(request):
    blog = Blog.objects.all()
    return render(request, 'Blog.html', {'blog': blog})
def HalamanMentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'Mentee.html', {'mentee': mentee})
def HalamanMentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'Mentor.html', {'mentor': mentor})
def HalamanAuthor(request):
    return render(request, 'Author.html')
def Halamanbase(request):
    return render(request, 'base/base.html')

def Input_mentor(request):
    if request.method == "POST":
        form = InputMentor(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputMentor()
    return render(request, 'Mentor-input.html', {'formMentor': form})

def Input_mentee(request):
    if request.method == "POST":
        form = InputMentee(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputMentee()
    return render(request, 'Mente-input.html', {'formMente': form})

def Input_blog(request):
    if request.method == "POST":
        form = InputBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputBlog()
    return render(request, 'Blog-input.html', {'formBlog': form})