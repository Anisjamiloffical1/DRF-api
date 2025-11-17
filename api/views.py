from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def StudentsView(request):
    students = {
        'id' : 1,
        'name' : 'Anis jamil',
        'age' : '20',
        'skills' : ['python', 'django', 'rest framework']

    }
    return JsonResponse(students)