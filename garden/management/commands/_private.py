from garden import models
from django.contrib.auth.models import User, Group, Permission

from random import randint, choice
from faker import Faker
fake = Faker()


PASSWORD = "garden2023"
GARDENS = [
'The River Gardens',
'The Royal Abundance Gardens',
'The Great Exemplary Botanical Garden',
'The Grand Arboreal Gardens',
'The Glorious Garden',
'The Daydon Hanging Botanical Garden',
]
DESC = "assdhashdasdhasudd sdhasdkhakjdhakd asdjasdjkasdjgasd adasdasdgasd asdasds das"

AREA_NR = 10
JOB_NR = 10
SPEC_NR = 10
TASK_NR = 10
EMP_NR = 4

PERMS = ["view", "add", "change"]
MODELS = ["job", "task", "worker", "location", "area"]


def cr_mail(name, surname):
    mail = f"{name}.{surname}@garden.com"
    i = 1
    while mail in User.objects.values_list('username', flat=True):
        mail = f"{name}.{surname}{1}@garden.com"
        i += 1
    return mail


def add_sup_group():
    group, created = Group.objects.get_or_create(name="supervisor")
    perm_to_add = []
    for model in MODELS:
        for p in PERMS:
            perm_to_add.append(Permission.objects.get(codename=p+"_"+model))
    group.permissions.add(*perm_to_add)
    return group


def add_supervisor():
    name, surname = "sup", "sup"
    user = User.objects.create_user(cr_mail(name, surname), password=PASSWORD)
    models.Supervisor.objects.create(name=name, surname=surname, user=user)
    gr = add_sup_group()
    user.groups.add(gr)
    user.save()


def add_locations():
    for garden in GARDENS:
        models.Location.objects.create(name=garden)


def add_areas():
    for _ in range(AREA_NR):
        models.Area.objects.create(location_id=randint(1, len(GARDENS)))


def add_jobs():
    for i in range(JOB_NR):
        models.Job.objects.create(name=f"Job no {i}", area_id=randint(1, AREA_NR), supervisor_id=1)


def add_specializations():
    for i in range(SPEC_NR):
        models.Specialization.objects.create(name=f"Specialization {i}")


def add_tasks():
    jobs = models.Job.objects.all()
    spec = models.Specialization.objects.all()
    for _ in range(TASK_NR):
        models.Task.objects.create(realization_date=fake.date(), description=DESC, job=choice(jobs), specialization=choice(spec))


def add_employees():
    for _ in range(EMP_NR):
        name, surname = fake.name().split(" ")
        mail = cr_mail(name, surname)
        specializations = models.Specialization.objects.all()
        user = User.objects.create_user(username=mail, password=PASSWORD)
        emp = models.Worker.objects.create(name=name, surname=surname, supervisor_id=1, user=user)
        a, b = randint(1, SPEC_NR), randint(1, SPEC_NR)
        emp.specializations.add(*specializations[min(a, b): max(a, b)])
        emp.save()


def add_emp_task():
    name, surname = "emp", "emp"
    mail = cr_mail(name, surname)
    user = User.objects.create_user(username=mail, password=PASSWORD)
    emp = models.Worker.objects.create(name=name, surname=surname, supervisor_id=1, user=user)
    emp.specializations.add("Specialization 1")
    emp.save()
    models.Task.objects.create(realization_date=fake.date(), description=DESC, job_id=randint(1, JOB_NR),
                               specialization_id=f"Specialization 1", worker=emp)



