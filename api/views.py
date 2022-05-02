# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView, CreateAPIView


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
