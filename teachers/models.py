from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100, blank=True)
    subjects = models.ManyToManyField('subjects.Subject', blank=True, related_name='teachers')
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"