from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ['roll_no']

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
