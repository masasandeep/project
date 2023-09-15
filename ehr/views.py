from django.shortcuts import render,redirect
from .models import *
from .forms import *
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
def create(request):
    form = TestcategoriesForm()
    if request.method=='POST':
        form = TestcategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all tests')
    context = {'form':form}
    return render(request,'ehr/create.html',context)
def reports(request):
    return render(request,'ehr/reports.html')
def upload(request):
    form = ReportForm()
    if request.method=='POST':
        images = request.FILES.getlist('images')
        name = request.POST.get('Testname')
        for image in images:
            Reports.objects.create(
                Testname = name,
                image = image
            )
        return redirect('report')
    context = {'forms':form,'type':'upload'}
    return render(request,'ehr/reports.html',context)
def Allreports(request):
    test = Reports.objects.all()
    return render(request,'ehr/reports.html',{'test':test,'type':'all'})
def ViewReport(request,pk):
    test = Reports.objects.get(Testname=pk)
    context = {'form': test,'type':'view'}
    return render(request,'ehr/reports.html',context)