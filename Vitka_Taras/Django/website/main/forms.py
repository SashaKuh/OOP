# main/forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'author', 'rating', 'release_date', 'description']  # Додайте release_date
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})  # Використання віджета для дати
        }
