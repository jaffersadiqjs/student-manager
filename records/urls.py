from django.urls import path
from .views import (
    fbv_student_list,
    StudentListView, StudentDetailView,
    StudentCreateView, StudentUpdateView, StudentDeleteView
)

urlpatterns = [
    path('fbv/', fbv_student_list, name='fbv-student-list'),
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]
