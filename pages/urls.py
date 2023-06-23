from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('grants/', views.GrantListView, name='grants'),
    path('grants/<int:pk>/', views.GrantDetailView, name='grant_detail'),

    path('students/by_grant/<int:grant_id>/',
         views.StudentListView, name='students'),
    path('students/<int:pk>/', views.StudentDetailView, name='student_detail')

]
