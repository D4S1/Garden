from django.urls import path
from . import views

app_name = 'garden'
urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('main', views.MainView.as_view(), name="main"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('list-jobs', views.ListJobsView.as_view(), name="list-jobs"),
    path('list-locations', views.ListLocationsView.as_view(), name="list-locations"),
    path('list-areas', views.ListAreasView.as_view(), name="list-areas"),
    path('list-employees', views.ListEmployeesView.as_view(), name="list-employees"),
    path('add-job', views.AddJobView.as_view(), name="add-job"),
    path('add-location', views.AddLocationView.as_view(), name="add-location"),
    path('add-area', views.AddAreaView.as_view(), name="add-area"),
    path('add-employee', views.AddEmployeeView.as_view(), name="add-employee"),

]
