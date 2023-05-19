from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.full_name,
                'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
            })
        return Response({'error': 'Invalid credentials'})
