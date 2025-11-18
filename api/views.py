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
@api_view(['GET', 'POST'])
def StudentsView(request):
    if request.method == 'GET':
        # Get all the data from Student Table
        students = Student.objects.all()
        serializers = StudentSerializers(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    # this use for api save in database
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# this use for api to get single student data in json format
@api_view(['GET'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seriliazer = StudentSerializers(student)
        return Response(seriliazer.data, status=status.HTTP_200_OK)

