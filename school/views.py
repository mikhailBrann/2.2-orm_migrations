from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    context['object_list'] = [{'name': student.name, 'group': student.group, 'teacher': student.get_teacher()} for student in Student.objects.all().order_by(ordering)]

    return render(request, template, context)