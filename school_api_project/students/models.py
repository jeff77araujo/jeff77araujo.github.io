from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Sala {self.number}"

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    first_semester_grade = models.FloatField()
    second_semester_grade = models.FloatField()
    teacher = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return self.name
