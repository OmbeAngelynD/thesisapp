from django.urls import path
from .views import student_view, thesis_view, adviser_view

urlpatterns = [
    path('students/', student_view.as_view(), name='student-list'),
    path('thesis/', thesis_view.as_view(), name='thesis-list'),
    path('adviser/', adviser_view.as_view(), name='adviser-list'),
]