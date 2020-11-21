# -*- coding: utf-8 -*-
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    """inside the Meta class we specify the characteristics of the table,
     which we then pass to views for display in create.html"""

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']  # specify which fields should be rendered inside the form
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of article'

            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of article'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full text of article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd hh:mm:ss'

            })
        }
