from django.shortcuts import render, redirect
from .models import Mark
from students.models import Student
from subjects.models import Subject


def marks_list(request):
    marks = Mark.objects.select_related("student", "subject").all()
    return render(request, "marks/list.html", {"marks": marks})


def marks_add(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        score = request.POST.get("score")

        Mark.objects.update_or_create(
            student_id=student_id,
            subject_id=subject_id,
            defaults={"score": score}
        )

        return redirect("marks_list")

    return render(request, "marks/add.html", {
        "students": students,
        "subjects": subjects
    })
