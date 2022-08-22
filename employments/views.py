from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from .models import EmploymentsPost
from django.views.generic import ListView, DetailView, UpdateView, CreateView


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
    success_url = reverse_lazy('employments:detail')

    def get_success_url(self):
        return reverse('employments:detail', kwargs={'pk':self.object.pk})


class EmploymentsPostCreateView(CreateView):
    model = EmploymentsPost
    fields = [
        'employments_position',
        'employments_compensation',
        'employments_text',
        'employments_tech_to_use',

        'company_id',
    ]
    success_url = reverse_lazy('employments:detail')

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated():
            form.instance.employments_author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/employments/')

    def get_success_url(self):
        return reverse('employments:detail', kwargs={'pk':self.object.pk})
