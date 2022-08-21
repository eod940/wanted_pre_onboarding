from django.shortcuts import render
from django.http import HttpResponse
from .models import EmploymentsPost
from django.views.generic import ListView, DetailView


class EmploymentsPostListView(ListView):
    model = EmploymentsPost


class EmploymentsPostDetailView(DetailView):
    model = EmploymentsPost
