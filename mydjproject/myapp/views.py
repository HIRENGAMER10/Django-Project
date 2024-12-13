from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm

# Create your views here.
def homepage(request):
    return HttpResponse('<h1 style="color:red;"> Home </h1>')

def addStudent(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request,'add.html',context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect(addStudent) 
        else:
            return render(request, 'add.html', {'form': form})

def displayStudent(request):
    dbdata = Student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'display.html',context)

def homepage(request):
    return render(request, 'home.html')
def aboutpage(request):
    return render(request, 'about.html')
def contactpage(request):
    return render(request, 'contact.html')
def formpageview(request):
    return render(request, 'form.html')

def formpageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return render(request,'ans.html',{'mya':a,'myb':b,'sum':c})