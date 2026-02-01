from django.db import models
from students.models import Student
from subjects.models import Subject


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "subject")

    def percentage(self):
        return self.score

    def grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 75:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.student} - {self.subject}"
