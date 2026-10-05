from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "category", "price", "description", "cover"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Book title"}),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Author name"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "cover": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }