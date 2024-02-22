from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from thesis_app.models import Student, Thesis, Advisor

class student_view(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    
class thesis_view(ListView):
    model = Thesis
    context_object_name = 'thesis'
    template_name = 'thesis_list.html'
    
class adviser_view(ListView):
    model = Advisor
    context_object_name = 'adviser'
    template_name = 'adviser_list.html'


def home(request):
    return render(request, 'base.html')