from django.db import models



class Award(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	date_awarded = models.DateField()

class Fee(models.Model):
	student = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	due_date = models.DateField()
	paid = models.BooleanField(default=False)

class Event(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField()
	description = models.TextField(blank=True)

class Lesson(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	duration_minutes = models.IntegerField()
	teacher = models.CharField(max_length=100)
	class_name = models.CharField(max_length=100)

class Class(models.Model):
	name = models.CharField(max_length=100)
	total_students = models.IntegerField()
	department = models.CharField(max_length=100)
