from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import CustomUser
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


@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Login user",
    request_body=openapi.Schema(
        required=['id'],
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='CustomUser ID'),
        }
    ),
    responses={
        200: openapi.Response(
            description="Get student by CustomUser ID",
            examples={
                'application/json': {
                    "image": "null",
                    "group": "20.07",
                    "course": "1",
                    "passport_number": "AB1234567",
                    "idcart_number": "AD1234567",
                    "passport_or_idcart_file": "null",
                    "status": "false",
                    "region": "Farg'ona",
                    "district": "Quva",
                    "street": "Topvoldi",
                    "resume": "null",
                    "base_student": "12",
                    "sub_faculty": "null"
                }
            }
        ),
        400: openapi.Response(
            description="Bad request",
            examples={
                'application/json': {
                        'error': 'Invalid credentials'
                }
            }
        )
    }
)
def get_student_by_base(request, pk):
    try:
        student = models.Student.objects.get(base_student__id=pk)
    except:
        return Response({"detail": "The associated student object does not exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)