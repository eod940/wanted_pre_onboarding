from django.shortcuts import render
from django.http import HttpResponse
from .models import EmploymentsPost
from django.views.generic import ListView, DetailView, UpdateView


class EmploymentsPostListView(ListView):
    model = EmploymentsPost


class EmploymentsPostDetailView(DetailView):
    model = EmploymentsPost


class EmploymentsPostUpdateView(UpdateView):
    model = EmploymentsPost
    fields = [
        'employments_position',
        'employments_compensation',
        'employments_text',
        'employments_tech_to_use',
    ]
    success_url = '/employments'
