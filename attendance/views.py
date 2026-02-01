from django.shortcuts import render, redirect
from students.models import Student
from subjects.models import Subject
from .models import Attendance
from datetime import date


def attendance_list(request):

    students = Student.objects.all()
    subjects = Subject.objects.all()

    selected_subject = request.GET.get("subject")
    selected_date = request.GET.get("date") or date.today()

    if request.method == "POST":
        subject_id = request.POST.get("subject")
        att_date = request.POST.get("date")

        subject = Subject.objects.get(id=subject_id)

        for s in students:
            present = request.POST.get(f"student_{s.id}") == "on"

            Attendance.objects.update_or_create(
                student=s,
                subject=subject,
                date=att_date,
                defaults={"present": present}
            )

        return redirect("attendance_list")

    return render(request, "attendance/list.html", {
        "students": students,
        "subjects": subjects,
        "today": selected_date
    })
