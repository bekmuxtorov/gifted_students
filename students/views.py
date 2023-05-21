from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


# ************************************************************************************************ #


# Faculty List API View
class FacultyListAPIView(generics.ListAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    search_fields = ('name',)


# Faculty Detail API View
class FacultyDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer


# ************************************************************************************************ #


# SubFaculty List API View
class SubFacultyListAPIView(generics.ListAPIView):
    queryset = models.SubFaculty.objects.all()
    serializer_class = serializers.SubFacultySerializer
    search_fields = ('name',)


# SubFaculty Detail API View
class SubFacultyDetailAPIView(generics.RetrieveAPIView):
    queryset = models.SubFaculty.objects.all()
    serializer_class = serializers.SubFacultySerializer


# ************************************************************************************************ #


# Student Create API View
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# Student List API View
class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    search_fields = ('get_full_name',)


# Student Detail API View
class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# Student Update API View
class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# ************************************************************************************************ #


# Article Create API View
class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


# Article List API View
class ArticleListAPIView(generics.ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    search_fields = ('name',)


# Article Detail API View
class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


# Article Update API View
class ArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


# Article Delete API View
class ArticleDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


# ************************************************************************************************ #


# Win Create API View
class WinCreateAPIView(generics.CreateAPIView):
    queryset = models.Win.objects.all()
    serializer_class = serializers.WinSerializer


# Win List API View
class WinListAPIView(generics.ListAPIView):
    queryset = models.Win.objects.all()
    serializer_class = serializers.WinSerializer
    search_fields = ('name',)


# Article Detail API View
class WinDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Win.objects.all()
    serializer_class = serializers.WinSerializer


# Win Update API View
class WinUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Win.objects.all()
    serializer_class = serializers.WinSerializer


# Article Delete API View
class WinDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Win.objects.all()
    serializer_class = serializers.WinSerializer
