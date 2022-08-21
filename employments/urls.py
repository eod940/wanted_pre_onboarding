from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmploymentsPostListView.as_view()),
    path('<int:pk>/', views.EmploymentsPostDetailView.as_view()),
]
