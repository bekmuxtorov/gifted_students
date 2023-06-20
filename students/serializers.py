from rest_framework import serializers

from . import models


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'


class SubFacultySerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = models.SubFaculty
        fields = '__all__'


class StudentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)
    subfaculty = SubFacultySerializer(read_only=True)

    class Meta:
        model = models.Student
        fields = '__all__'
        


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class WinSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Win
        fields = '__all__'
