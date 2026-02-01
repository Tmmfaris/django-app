from django.shortcuts import render, redirect
def teacher_create(request):
	# Placeholder view for Add Teacher
	return render(request, 'teachers/teacher_form.html')
from django.shortcuts import render



from students.models import Student, Parent
from teachers.models import Teacher
from departments.models import Department
from subjects.models import Subject

def home(request):
	return render(request, 'dashboard.html')

def teacher_dashboard(request):
	return render(request, 'dashboard.html')

def student_dashboard(request):
	return render(request, 'dashboard.html')

def departments(request):
	departments = Department.objects.all()
	return render(request, 'departments/department_list.html', {'departments': departments})

def subjects(request):
	subjects = Subject.objects.all()
	return render(request, 'subjects/subject_list.html', {'subjects': subjects})

def accounts(request):
	return render(request, 'accounts/account_list.html')

def holiday(request):
	return render(request, 'holiday/holiday_list.html')

def fees(request):
	return render(request, 'fees/fee_list.html')

def exams(request):
	return render(request, 'exams/exam_list.html')

def events(request):
	return render(request, 'events/event_list.html')

def teachers(request):
	teachers = Teacher.objects.all()
	return render(request, 'teachers/teacher_list.html', {'teachers': teachers})
