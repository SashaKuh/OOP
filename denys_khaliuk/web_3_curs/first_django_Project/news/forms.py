from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс',
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст',
            }),

        }