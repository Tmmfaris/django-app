from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/list.html", {"teachers": teachers})


def teacher_add(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("teacher_list")

    return render(request, "form.html", {
        "form": form,
        "title": "Add Teacher"
    })


def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)

    if form.is_valid():
        form.save()
        return redirect("teacher_list")

    return render(request, "form.html", {
        "form": form,
        "title": "Edit Teacher"
    })


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect("teacher_list")
