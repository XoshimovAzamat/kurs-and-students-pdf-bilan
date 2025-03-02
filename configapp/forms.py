import re
from django import forms
from django.core.exceptions import ValidationError
from .models import *


# class NewForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Yangilik nomi',
#                             widget=forms.TextInput(attrs={"class":"form-control"}))
#     context = forms.CharField(label="Yangilik haqida", required=False,
#                             widget=forms.Textarea(attrs={"class":"form-control",
#                                                             "rows": 5 }))
#     is_bool= forms.BooleanField(label="Nashr etish", initial=True)
#
#     category= forms.ModelChoiceField(empty_label="Qaysi tur?", label="Yangilik turi", queryset=Categories.objects.all(),
#                                      widget=forms.Select(attrs={"class":"form-control"}))
#

class AddKurs(forms.ModelForm):
    class Meta:
        model = Kurs
        # fields = '__all__'
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError("Title raqam bo`lmasin!")
            return title


class AddStudent(forms.ModelForm):
    # kurs = forms.ModelMultipleChoiceField(
    #     queryset=Kurs.objects.all(),
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    # )

    class Meta:
        model = Student
        fields = ['name', 'sur_name', 'age', 'phone', 'email', 'kurs']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sur_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'kurs': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
