# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView, CreateAPIView


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
