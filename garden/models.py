from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=64, primary_key=True, unique=True)


class Supervisor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    @property
    def login(self):
        return f"{self.name}.{self.surname}@ogrodnicy.bd"

    @property
    def password(self):
        return f"Kierownik{self.pk}"

    def __str__(self):
        return f"SV {self.name} {self.surname}"


class Worker(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)

    @property
    def login(self):
        return f"{self.name}.{self.surname}@ogrodnicy.bd"

    @property
    def password(self):
        return f"Ogrodnik{self.pk}"

    def __str__(self):
        return f" W {self.name} {self.surname}"


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Area(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Area no. {self.pk}"


class Job(models.Model):
    name = models.CharField(max_length=128)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, null=True, on_delete=models.SET_NULL)


class Task(models.Model):
    realization_date = models.DateField()
    description = models.TextField(null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, null=True, on_delete=models.SET_NULL)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

