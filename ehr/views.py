from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
def Alltests(request):
    test = Testcategories.objects.all()
    context = {'test':test}
    return render(request,'ehr/home.html',context)
def search(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    name = Testcategories.objects.filter(
        Q(name__icontains = q)
    )
    context = {'test':name}
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
        files = request.FILES.getlist('files')
        name = request.POST.get('Testname')
        for file in files:
            Reports.objects.create(
                Testname = name,
                file = file
            )
        return redirect('reportsection')
    context = {'forms':form,'type':'upload'}
    return render(request,'ehr/upload.html',context)
def viewReports(request):
    test = Reports.objects.all()
    return render(request,'ehr/view-reports.html',{'pdf_files':test})
def download_pdf(request,pk):
    pdf_file = get_object_or_404(Reports, pk=pk)
    file_path = pdf_file.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response