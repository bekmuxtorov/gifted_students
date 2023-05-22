from rest_framework import generics

from . import serializers
from . import models


# ************************************************************************************************ #


# Grant Create API View
class GrantCreateAPIView(generics.CreateAPIView):
    queryset = models.Grant.objects.all()
    serializer_class = serializers.GrantSerializer


# Grant List API View
class GrantListAPIView(generics.ListAPIView):
    queryset = models.Grant.objects.all()
    serializer_class = serializers.GrantSerializer
    search_fields = ('name',)


# Grant Detail API View
class GrantDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Grant.objects.all()
    serializer_class = serializers.GrantSerializer


# Grant Update API View
class GrantUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Grant.objects.all()
    serializer_class = serializers.GrantSerializer


# Grant Delete API View
class GrantDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Grant.objects.all()
    serializer_class = serializers.GrantSerializer


# ************************************************************************************************ #


# Result Create API View
class ResultCreateAPIView(generics.CreateAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer


# Win List API View
class ResultListAPIView(generics.ListAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    search_fields = ('student__get_full_name',)


# Result Detail API View
class ResultDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer


# Result Update API View
class ResultUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer


# Result Delete API View
class ResultDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer


# ************************************************************************************************ #


# ScienceDirection Create API View
class ScienceDirectionCreateAPIView(generics.CreateAPIView):
    queryset = models.ScienceDirection.objects.all()
    serializer_class = serializers.ScienceDirectionSerializer


# ScienceDirection List API View
class ScienceDirectionListAPIView(generics.ListAPIView):
    queryset = models.ScienceDirection.objects.all()
    serializer_class = serializers.ScienceDirectionSerializer
    search_fields = ('research_advisor',)


# ScienceDirection Detail API View
class ScienceDirectionDetailAPIView(generics.RetrieveAPIView):
    queryset = models.ScienceDirection.objects.all()
    serializer_class = serializers.ScienceDirectionSerializer


# ScienceDirection Update API View
class ScienceDirectionUpdateAPIView(generics.UpdateAPIView):
    queryset = models.ScienceDirection.objects.all()
    serializer_class = serializers.ScienceDirectionSerializer


# ScienceDirection Delete API View
class ScienceDirectionDeleteAPIView(generics.DestroyAPIView):
    queryset = models.ScienceDirection.objects.all()
    serializer_class = serializers.ScienceDirectionSerializer
