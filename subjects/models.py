from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name