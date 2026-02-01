from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from marks.models import Mark
from attendance.models import Attendance


def dashboard(request):

    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "subject_count": Subject.objects.count(),
        "marks_count": Mark.objects.count(),
        "attendance_count": Attendance.objects.count(),
    }

    return render(request, "dashboard.html", context)


# ✅ ADD THIS — student dashboard (simple version)
def student_dashboard(request):
    return render(request, "student_dashboard.html")
