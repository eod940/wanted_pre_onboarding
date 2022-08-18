from django.shortcuts import render
from django.http import HttpResponse
from .models import EmploymentsPost
from django.views.generic import ListView


def index(request):
    return HttpResponse("안녕하세요")


class EmploymentsPostListView(ListView):
    model = EmploymentsPost

    def get_queryset(self):
        return EmploymentsPost.objects.orderd_by('-employments_created')