from django.http import HttpResponse
from django.shortcuts import render, redirect

from Etudiants.forms import StudentForm
from Etudiants.models import Student


def addandshow(request):
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = Student(name=name, email=email, password=password)
            reg.save()
            form = StudentForm()
        else:
            context["errors"] = form.errors
    form = StudentForm()
    context["form"] = form
    listStudent = Student.objects.all()
    context["listStudent"] = listStudent
    return render(request, 'etudiant/addandshows.html', context=context)

def update_student(request, id):
    if request.method == 'POST':
        update_student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=update_student)
        if form.is_valid():
            form.save()
            return redirect('addandshows')
        #else:
    update_student = Student.objects.get(pk=id)
    form = StudentForm(instance=update_student)
    return render(request, "etudiant/updatestudent.html", context={"form": form})


def delete_student(request, id):
    if request.method == 'POST':
        search_student = Student.objects.get(pk=id)
        search_student.delete()
        return redirect('addandshows')
