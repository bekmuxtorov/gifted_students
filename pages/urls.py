from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('grants/', views.GrantListView, name='grants'),
    path('grants/<int:pk>/', views.GrantDetailView, name='grant_detail'),
    path('grants/new/', views.create_grant, name='create_grant'),
    path('grants/update/<int:pk>/', views.update_grant, name="update_grant"),
    path('grants/delete/<int:pk>/', views.delete_grant, name="delete_grant"),

    path('students/by_grant/<int:grant_id>/',
         views.StudentListView, name='students'),
    path('students/<int:pk>/', views.StudentDetailView, name='student_detail'),

]
