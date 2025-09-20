from django import forms
from models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)