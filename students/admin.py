from django.contrib import admin


from .models import Student, Parent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'student_id', 'gender', 'parent', 'class_name')
	search_fields = ('first_name', 'last_name', 'student_id', 'class_name')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
	list_display = ('father_name', 'father_occupation', 'mother_name', 'phone')
	search_fields = ('father_name', 'mother_name', 'phone')
