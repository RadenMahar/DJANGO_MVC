from django import forms
from .models import Mentor, Mentee, Blog

class InputMentor(forms.ModelForm):

    class Meta:
        model = Mentor
        fields = ('nama', 'jobStatus', 'moto', 'picture')

class InputMentee(forms.ModelForm):

    class Meta:
        model = Mentee
        fields = ('nama', 'picture', 'moto')
    
class InputBlog(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('picture', 'date', 'head', 'text')