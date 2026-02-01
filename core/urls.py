from django.urls import path
from . import views
from students.views import student_list

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('departments/', views.departments, name='departments'),
    path('subjects/', views.subjects, name='subjects'),
    path('accounts/', views.accounts, name='accounts'),
    path('holiday/', views.holiday, name='holiday'),
    path('fees/', views.fees, name='fees'),
    path('exams/', views.exams, name='exams'),
    path('events/', views.events, name='events'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/add/', views.teacher_create, name='teacher_create'),
    path('students/', student_list, name='student_list'),
]
