from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('faculty/create', views.list_create_faculty, name='list_create_faculty'),
    path('faculty/update/<int:pk>/', views.update_facult, name='update_faculty'),
    path('faculty/delete/<int:pk>/', views.delete_faculty, name='delete_faculty'),

    path('direction/create/', views.list_create_subfaculty, name='list_create_subfaculty'),
    path('direction/update/<int:pk>/', views.update_subfaculty, name='update_subfaculty'),
    path('direction/delete/<int:pk>/', views.delete_subfaculty, name='delete_subfaculty'),

    path('logout/', views.logout_view, name='logout'),
    path('grants/', views.GrantListView, name='grants'),
    path('grants/<int:pk>/', views.GrantDetailView, name='grant_detail'),
    path('grants/new/', views.create_grant, name='create_grant'),
    path('grants/update/<int:pk>/', views.update_grant, name="update_grant"),
    path('grants/delete/<int:pk>/', views.delete_grant, name="delete_grant"),
    path('students/by_grant/<int:grant_id>/', views.StudentListView, name='students'),
    path('students/<int:pk>/', views.StudentDetailView, name='student_detail'),
    path('faculties/', views.FacultyListView, name='faculties'),

    path('messages/', views.list_create_message, name="messages_list"),
]


