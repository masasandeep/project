from django.forms import ModelForm
from .models import *
class ResultsForm(ModelForm):
    class Meta:
        model = TestResults
        fields = '__all__'
        exclude = ['category']