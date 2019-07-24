from django.contrib import admin
from .models import Mentee, Mentor, Blog

# Register your models here.
class MenteeDisplay(admin.ModelAdmin):
    list_display = ['nama', 'picture', 'moto']

class MentorDisplay(admin.ModelAdmin):
    list_display = ['nama', 'jobStatus', 'moto', 'picture']

class BlogDisplay(admin.ModelAdmin):
    list_display = ['picture', 'date', 'head']

admin.site.register(Mentee, MenteeDisplay)
admin.site.register(Mentor, MentorDisplay)
admin.site.register(Blog, BlogDisplay)
