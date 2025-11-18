from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
# this use for api to get all students data in json format manual this not recommended for large data use django rest framework

# def StudentsView(request):
#     students = Student.objects.all()
#     student_list = list(students.values())
      
#     return JsonResponse(student_list, safe=False)
@api_view(['GET'])
def StudentsView(request):
    if request.method == 'GET':
        # Get all the data from Student Table
        students = Student.objects.all()
        serializers = StudentSerializers(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

