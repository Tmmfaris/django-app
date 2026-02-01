from django.db import models


from students.models import Student
from django.db import models

class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.DateField()
	present = models.BooleanField(default=True)

	class Meta:
		unique_together = ('student', 'date')

	def __str__(self):
		return f"{self.student} - {self.date} - {'Present' if self.present else 'Absent'}"
