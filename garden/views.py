from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "main.html")


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("garden:main")
        return render(request, "login.html")


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('garden:login')


class ListJobsView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.groups.filter(name='supervisor').exists() or request.user.is_superuser:
            jobs = models.Job.objects.all()
        else:
            jobs = []
            for task in models.Task.objects.filter(worker=models.Worker.objects.get(user=request.user)):
                if task.job.pk not in jobs:
                    jobs.append(task.job.pk)
            jobs = models.Job.objects.filter(pk__in=jobs)
        return render(request, "list_jobs.html", {'jobs': jobs})


class AddJobView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.add_job'

    def get(self, request):
        supervisors = models.Supervisor.objects.all()
        areas = models.Area.objects.all()
        return render(request, "add_job.html", {'areas': areas, 'supervisors': supervisors})

    def post(self, request):
        name = request.POST['name']
        area = request.POST['area']
        supervisor = request.POST['supervisor']
        if area and name and supervisor:
            models.Job.objects.create(name=name, area_id=area, supervisor_id=supervisor)
            return redirect("garden:list-jobs")
        return render(request,  "add_jobs.html", {'lack': True})


class ListLocationsView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.view_location'

    def get(self, request):
        locations = models.Location.objects.all()
        return render(request, "list_locations.html", {'locations': locations})


class AddLocationView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.add_location'

    def get(self, request):
        return render(request,  "add_location.html")

    def post(self, request):
        name = request.POST['name']
        if name and len(models.Location.objects.filter(name=name)) == 0:
            models.Location.objects.create(name=name)
            return redirect("garden:list-locations")
        return render(request,  "add_location.html", {'exist': True})


class ListAreasView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.view_area'

    def get(self, request):
        areas = models.Area.objects.all()
        return render(request, "list_areas.html", {'areas': areas})


class AddAreaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.add_area'

    def get(self, request):
        locations = models.Location.objects.all()
        return render(request,  "add_area.html", {'locations': locations})

    def post(self, request):
        location = request.POST['location']
        if location:
            models.Area.objects.create(location_id=location)
            return redirect("garden:list-areas")
        return render(request,  "add_area.html", {'lack': True})


class ListEmployeesView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.view_worker'

    def get(self, request):
        employees = models.Worker.objects.all()
        return render(request, "list_employees.html", {'employees': employees})


class AddEmployeeView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'garden.add_worker'

    def get(self, request):
        supervisors = models.Supervisor.objects.all()
        specializations = models.Specialization.objects.all()
        return render(request,  "add_employee.html", {'supervisors': supervisors, 'specializations': specializations})

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        supervisor = request.POST['supervisor']
        specializations = request.POST.getlist('specializations')
        if not name or not surname or not supervisor:
            return render(request, "add_area.html", {'lack': True})
        mail = f"{name}.{surname}@garden.com"
        i = 1
        while mail in User.objects.values_list('username', flat=True):
            mail = f"{name}.{surname}{i}@garden.com"
            i += 1
        user = User.objects.create_user(username=mail, email=mail, password="garden2023")
        emp = models.Worker.objects.create(name=name, surname=surname, supervisor_id=supervisor, user=user)
        emp.specializations.add(*specializations)
        emp.save()
        return redirect("garden:list-employees")
