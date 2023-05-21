from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers


# Create your views here.


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.full_name,
                'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
            })
        return Response({'error': 'Invalid credentials'})


class RegisterAPIView(APIView):
    serializer_class = serializers.UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
