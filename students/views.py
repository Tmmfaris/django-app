from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()

    paginator = Paginator(students, 10)
    page = request.GET.get("page")
    data = paginator.get_page(page)

    return render(request, "students/list.html", {"data": data})


def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "form.html", {"form": form, "title": "Add Student"})


def student_edit(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "form.html", {"form": form, "title": "Edit Student"})


def student_delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect("student_list")
