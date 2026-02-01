from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm


def subject_list(request):
    subjects = Subject.objects.select_related("teacher")
    return render(request, "subjects/list.html", {
        "subjects": subjects
    })


def subject_add(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("subject_list")

    return render(request, "form.html", {
        "form": form,
        "title": "Add Subject"
    })


def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)

    if form.is_valid():
        form.save()
        return redirect("subject_list")

    return render(request, "form.html", {
        "form": form,
        "title": "Edit Subject"
    })


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect("subject_list")
