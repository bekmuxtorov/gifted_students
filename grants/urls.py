from django.urls import path
from . import views


urlpatterns = [
    # 
    path('science-direction/create/', views.ScienceDirectionCreateAPIView.as_view()),
    path('science-direction/', views.ScienceDirectionListAPIView.as_view()),
    path('science-direction/<int:pk>/', views.ScienceDirectionDetailAPIView.as_view()),
    path('science-direction/<int:pk>/update/', views.ScienceDirectionUpdateAPIView.as_view()),
    path('science-direction/<int:pk>/delete/', views.ScienceDirectionDeleteAPIView.as_view()),

    # Result
    path('result/create/', views.ResultCreateAPIView.as_view()),
    path('result/', views.ResultListAPIView.as_view()),
    path('result/<int:pk>/', views.ResultDetailAPIView.as_view()),
    path('result/<int:pk>/update/', views.ResultUpdateAPIView.as_view()),
    path('result/<int:pk>/delete/', views.ResultDeleteAPIView.as_view()),

    # grant
    path('grant/create/', views.GrantCreateAPIView.as_view()),
    path('grant/', views.GrantListAPIView.as_view()),
    path('grant/<int:pk>/', views.GrantDetailAPIView.as_view()),
    path('grant/<int:pk>/update/', views.GrantUpdateAPIView.as_view()),
    path('grant/<int:pk>/delete/', views.GrantDeleteAPIView.as_view()),
]
