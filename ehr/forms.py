from django.forms import ModelForm
from .models import *
class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

class ResultsForm(ModelForm):
    class Meta:
        model = TestResults
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field=='category':
                field.widget.attrs.update({
                'class': 'form-select'
            })
            field.widget.attrs.update({
                'class': 'form-control'
            })
class TestcategoriesForm(ModelForm):
    class Meta:
        model = Testcategories
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TestcategoriesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field=='category':
                field.widget.attrs.update({
                'class': 'form-select'
            })
            field.widget.attrs.update({
                'class': 'form-control'
            })
class ReportForm(ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
