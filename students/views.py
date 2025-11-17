from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students_list = [{'id' : 1, 'name' : 'John Doe', 'id' : 2, 'name' : 'Jane Smith'}]
    return HttpResponse(students_list)