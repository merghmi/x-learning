from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Student, Prof, Inscription,Matiere,News


class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student
