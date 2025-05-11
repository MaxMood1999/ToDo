from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from rest_framework.viewsets import ViewSet

from .models import Category
from .serializers import RegisterSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema




class RegisterView(APIView):
    @extend_schema(request=RegisterSerializer, responses={201: RegisterSerializer})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Foydalanuvchi muvaffaqiyatli yaratildi!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @extend_schema(request=LoginSerializer, responses={200: LoginSerializer})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({'message': 'Tizimga muvaffaqiyatli kirdingiz!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.viewsets import ModelViewSet

from rest_framework.viewsets import ModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LastTaskAPIView(APIView):
    queryset = Task.objects.all().last()
    serializer_class = TaskSerializer
    def get(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)

class TodayTaskAPIView(APIView):
    queryset = Task.objects.all().filter(date=Task.objects.all().last().date)
    serializer_class = TaskSerializer



