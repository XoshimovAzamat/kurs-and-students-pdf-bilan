from django.db import models


class Kurs(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    sur_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(blank=True)
    kurs = models.ManyToManyField('Kurs')
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
