from django import forms
from django.forms.widgets import DateInput

from .models import Question


class QuestionForm(forms.ModelForm):
   class Meta:
       model = Question
       fields = '__all__'
       widgets = {
           'pub_date': DateInput(attrs={'type': 'date'}),
       }
