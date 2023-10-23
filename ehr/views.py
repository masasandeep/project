from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
def userProfile(request,pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method=='POST':
        form = UserForm(request.POST,instance = user)
        if form.is_valid():
            user1 = form.save(commit=False)
            user = User.objects.get(id=pk)
            user.set_password()
            return redirect('home')
    context = {'form': form}
    return render(request,'ehr/profile.html',context)
def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    test = Testcategories.objects.all()
    test = Testcategories.objects.filter(
        Q(division__name__icontains = q)
    )
    division = MainDivisions.objects.all()
    context = {'test':test,'division':division }
    return render(request,'ehr/home.html',context)
def delete(request,pk):
    test = Testcategories.objects.get(name=pk)
    results = TestResults.objects.filter(category = test).first()
    test.delete()
    results.delete()
    return redirect('home')
def search(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    name = Testcategories.objects.filter(
        Q(name__icontains = q)|
        Q(n1__icontains = q)|
        Q(n2__icontains = q)|
        Q(n3__icontains = q)|
        Q(n4__icontains = q)|
        Q(n5__icontains = q)|
        Q(n6__icontains = q)
    )
    context = {'test':name}
    return render(request,'ehr/home.html',context)
def test(request,pk):
    division = MainDivisions.objects.all()
    test = Testcategories.objects.all()
    test1 = Testcategories.objects.get(name=pk)
    results = TestResults.objects.filter(category = test1)
    forms = ResultsForm(instance = results.first())
    if request.method == 'POST':
        form = ResultsForm(request.POST or None, instance=results.first())
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'test1':test1,'test':test,'forms':forms,'results':results.first(),'division':division}
    return render(request,'ehr/test.html',context)
def create(request):
    division = MainDivisions.objects.all()
    test = Testcategories.objects.all()
    form = TestcategoriesForm()
    if request.method=='POST':
        form = TestcategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            test = test = Testcategories.objects.get(name = request.POST.get('name'))
            results = TestResults.objects.create(category = test)
            return redirect('home')
    context = {'form':form,'test':test,'division':division}
    return render(request,'ehr/create.html',context)
def reports(request):
    division = MainDivisions.objects.all()
    test = Testcategories.objects.all()
    return render(request,'ehr/reports.html',{'test':test,'division':division})
def upload(request):
    division = MainDivisions.objects.all()
    test = Testcategories.objects.all()
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
    context = {'forms':form,'type':'upload','test':test,'division':division}
    return render(request,'ehr/upload.html',context)
def viewReports(request):
    division = MainDivisions.objects.all()
    test = Testcategories.objects.all()
    report = Reports.objects.all()
    return render(request,'ehr/view-reports.html',{'pdf_files':report,'test':test,'division':division})
def download_pdf(request,pk):
    pdf_file = get_object_or_404(Reports, pk=pk)
    file_path = pdf_file.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response