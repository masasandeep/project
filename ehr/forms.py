from django.forms import ModelForm
from .models import *
class ResultsForm(ModelForm):
    class Meta:
        model = TestResults
        fields = '__all__'
        exclude = ['category']
class TestcategoriesForm(ModelForm):
    class Meta:
        model = Testcategories
        fields = '__all__'
class ReportForm(ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
