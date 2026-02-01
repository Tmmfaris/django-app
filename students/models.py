from django.db import models


from django.contrib.auth.models import User




class Parent(models.Model):
	father_name = models.CharField(max_length=100, default='')
	father_occupation = models.CharField(max_length=100, blank=True, default='')
	mother_name = models.CharField(max_length=100, blank=True, default='')
	present_address = models.TextField(blank=True, default='')
	phone = models.CharField(max_length=20, blank=True, default='')

	def __str__(self):
		return self.father_name


GENDER_CHOICES = [
	('Male', 'Male'),
	('Female', 'Female'),
]


class Student(models.Model):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	student_id = models.CharField(max_length=100, unique=True, default='')
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
	date_of_birth = models.DateField(null=True, blank=True)
	student_image = models.ImageField(upload_to='student_pics/', blank=True, null=True)
	parent = models.OneToOneField(Parent, on_delete=models.CASCADE, null=True, blank=True)
	slug = models.SlugField(unique=True, blank=True, default='')
	class_name = models.CharField(max_length=20, blank=True, default='')
	academic_history = models.TextField(blank=True, default='')

	def __str__(self):
		return f"{self.first_name} {self.last_name} - {self.student_id}"
