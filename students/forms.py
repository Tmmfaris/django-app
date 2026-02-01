from django import forms
from .models import Student, Parent

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['father_name', 'father_occupation', 'mother_name', 'present_address', 'phone']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_image', 'parent', 'slug', 'class_name', 'academic_history']
