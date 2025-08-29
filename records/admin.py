from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'course', 'age')
    search_fields = ('name', 'roll_no', 'course')
