from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm

# ----------------
# FBV for comparison
# ----------------
def fbv_student_list(request):
    students = Student.objects.all()
    return render(request, 'records/fbv_student_list.html', {'students': students})


# ----------------
# CBVs for CRUD
# ----------------
class StudentListView(ListView):
    model = Student
    template_name = 'records/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'records/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'records/student_form.html'
    success_url = reverse_lazy('records:student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'records/student_form.html'
    success_url = reverse_lazy('records:student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'records/student_confirm_delete.html'
    success_url = reverse_lazy('records:student-list')
