from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializers, EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics
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
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seriliazer = StudentSerializers(student)
        return Response(seriliazer.data, status=status.HTTP_200_OK)
# this use for api update single student data in json format
    
    elif request.method == 'PUT':
        seriliazer = StudentSerializers(student, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data, status=status.HTTP_200_OK)
        else:
            return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        student.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# this class use for api to get all students data in json format using class based views

# The class view automatically maps HTTP methods to class methods like get(), post(), put(), delete(), etc.
# class Employees(APIView):
#     # member function to handle GET request
#     def get(self, request):
#         employees = Employee.objects.all()
#         # this is use to serialize multiple objects
#         serializers = EmployeeSerializers(employees, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    
#     # this member function to handle POST request
#     def post(self, request):
#         serializers = EmployeeSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) # this is use for error response
        
#     # this 
# class EmployeeDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Http404
        
#     def get(self, request, pk):
#         employees = self.get_object(pk)
#         serializers = EmployeeSerializers(employees)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         emoloyees = self.get_object(pk)
#         serializers = EmployeeSerializers(emoloyees, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_200_OK)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# using mixins and generics class based views for employee api
"""
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
# this use for single employee details api
class EmployeeDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # this use for get single employee details api
    def get(self, request, pk):
        return self.retrieve(request, pk)
    # this use for update single employee details api
    def put(self, request, pk):
        return self.update(request, pk)
    # this use for delete single employee details api
    def delete(self, request, pk):  
        return self.destroy(request, pk)
        """

# using generics class based views for employee api

class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


# this use for single employee details api\
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'