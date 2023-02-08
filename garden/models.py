from django.db import models
from django.contrib.auth.models import User


class Specialization(models.Model):
    name = models.CharField(max_length=64, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Worker(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Area(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}"


class Job(models.Model):
    name = models.CharField(max_length=128)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Task(models.Model):
    realization_date = models.DateField()
    description = models.TextField(null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, null=True, on_delete=models.SET_NULL)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

