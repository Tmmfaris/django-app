from django.db import models


from students.models import Student
from django.db import models

class Subject(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name

class Marks(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	exam_name = models.CharField(max_length=50)
	marks_obtained = models.FloatField()
	max_marks = models.FloatField()
	date = models.DateField()

	class Meta:
		unique_together = ('student', 'subject', 'exam_name', 'date')

	def __str__(self):
		return f"{self.student} - {self.subject} - {self.exam_name}: {self.marks_obtained}/{self.max_marks}"
