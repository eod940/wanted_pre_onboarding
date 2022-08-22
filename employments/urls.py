from django.urls import path
from . import views

app_name = "employments"

urlpatterns = [
    path('', views.EmploymentsPostListView.as_view()),
    path('<int:pk>/', views.EmploymentsPostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.EmploymentsPostUpdateView.as_view(), name='update'),
    path('create/', views.EmploymentsPostCreateView.as_view(), name='create'),
]
