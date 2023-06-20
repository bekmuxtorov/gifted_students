from django.urls import path
from . import views


urlpatterns = [
    # Faculty
    path('faculties/', views.FacultyListAPIView.as_view()),
    path('faculties/<int:pk>/', views.FacultyDetailAPIView.as_view()),

    # SubFaculty
    path('sub-faculties/', views.SubFacultyListAPIView.as_view()),
    path('sub-faculties/<int:pk>/', views.SubFacultyDetailAPIView.as_view()),

    # Students
    path('students/create/', views.StudentCreateAPIView.as_view()),
    path('students/', views.StudentListAPIView.as_view()),
    path('students/<int:pk>/', views.StudentDetailAPIView.as_view()),
    path('students/<int:pk>/update/', views.StudentUpdateAPIView.as_view()),

    # Get Student by CustomUser
    path('students/by_customuser/<int:pk>/', views.get_student_by_base),

    # Articles
    path('articles/create/', views.ArticleCreateAPIView.as_view()),
    path('articles/', views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', views.ArticleDetailAPIView.as_view()),
    path('articles/<int:pk>/update/', views.ArticleUpdateAPIView.as_view()),
    path('articles/<int:pk>/delete/', views.ArticleDeleteAPIView.as_view()),

    # Wins
    path('student-wins/create/', views.WinCreateAPIView.as_view()),
    path('student-wins/', views.WinListAPIView.as_view()),
    path('student-wins/<int:pk>/', views.WinDetailAPIView.as_view()),
    path('student-wins/<int:pk>/update/', views.WinUpdateAPIView.as_view()),
    path('student-wins/<int:pk>/delete/', views.WinDeleteAPIView.as_view()),
]
