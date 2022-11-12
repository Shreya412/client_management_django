from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from django.contrib.auth.models import User
import jwt, datetime
from django.conf import settings


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
        


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
# from .serializers import UserSerializer, LoginSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings
# from django.contrib import auth
# import jwt
# # Create your views here.


# class RegisterView(GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         email = data.get('email', '')
#         password = data.get('password', '')
#         user = auth.authenticate(email=email, password=password)

#         if user:
#             auth_token = jwt.encode(
#                 {'email': user.email}, settings.JWT_SECRET_KEY, algorithm="HS256")

#             serializer = UserSerializer(user)

#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)

#             # SEND RES
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)