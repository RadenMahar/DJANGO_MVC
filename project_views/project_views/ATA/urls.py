from django.urls import path
from . import views

urlpatterns = [
    path('', views.HalamanHome, name = 'home'),
    path('blog/', views.HalamanBlog, name = 'blog'),
    path('mentee/', views.HalamanMentee, name = 'mentee'),
    path('mentor/', views.HalamanMentor, name = 'mentor'),
    path('author/', views.HalamanAuthor, name = 'author'),
    path('base/', views.Halamanbase, name = 'base'),
    path('inputmentor/', views.Input_mentor, name = 'MentorInput'),
    path('inputmentee/', views.Input_mentee, name = 'MenteeInput'),
    path('inputblog/', views.Input_blog, name = 'BlogInput')
]