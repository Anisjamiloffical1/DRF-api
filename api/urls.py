from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.StudentsView),
    path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view())
    path('', include(router.urls)),
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),
]