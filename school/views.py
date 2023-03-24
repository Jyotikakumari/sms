
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Students


def homepage(Req):
    form = StudentForm(Req.POST or None)
    data = {
        "students" : Students.objects.all(),
        "form" : form
    }

    if Req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    
    return render(Req,"index.html",data)


def deleteStudent(r, id):
    student = Students.objects.get(pk=id)
    student.delete()
    return redirect(homepage)

def editStudent(r,id):
    Student = Students.objects.get(pk=id)
    form = StudentForm(r.POST or None, instance=Student)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(r,"edit.html",{"form": form})   

def searchStudent(r):
    if r.method == "GET":
        search_query =r.GET.get("search")
        form = StudentForm()
        data = {
            "students" : Students.objects.filter(name__icontains=search_query),
            "form" : form
        }
        return render(r,"index.html",data)    
         

def filterCity(r):
    if r.method == "GET":
        search = r.GET.get("city")
        form = StudentForm()
        data ={
            "form": form,
            "students": Students.objects.filter(city=search)
        }
        return render(r,"index.html", data)
