from django import forms
from theater_lab.models import Actor, Director, Theater

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'date_of_birth']

class TheaterForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = ['name', 'address', 'number_of_halls']