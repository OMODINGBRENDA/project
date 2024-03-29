from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('service/', views.service, name='service'),
    path('students/', views.students_list, name='students_list'),
    path('teachers/', views.teachers, name='teachers.html')

]