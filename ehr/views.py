from django.shortcuts import render,redirect
from .models import *
from .forms import ResultsForm
# Create your views here.POST.
def Alltests(request):
    test = Testcategories.objects.all()
    context = {'test':test}
    return render(request,'ehr/home.html',context)
def test(request,pk):
    forms = ''
    test = Testcategories.objects.get(name=pk)
    results = TestResults.objects.filter(category = test)
    forms = ResultsForm(instance = results.first())
    if request.method == 'POST':
        form = ResultsForm(request.POST or None, instance=results.first())
        if form.is_valid():
            form.save()
            return redirect('all tests')
    context = {'test':test,'forms':forms,'results':results.first()}
    return render(request,'ehr/test.html',context)