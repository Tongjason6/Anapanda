from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.utils import timezone

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from django_filters.views import FilterView

from .models import Circle, Role, Task, Kummitment, RoleKummitment, Project
from .filters import TaskFilter

def kummithome(request):
    return render(request, 'managetime/home.html')

class CircleView(DetailView):
    model = Circle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CircleList(FilterView):
    model = Circle
    filter_fields = []
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TaskCreate(CreateView):
    model = Task
    fields = ['subject', 'description', 'doneevidence', 'startdate', 'deadline', 'project', 'role', 'circle']
   
    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['subject', 'description', 'doneevidence', 'startdate', 'deadline', 'project', 'role', 'circle']

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TaskList(FilterView):
    model = Task
    filter_fields = ['created_by', 'description', 'circle', 'project', 'role']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class KummitmentCreate(CreateView):
    model = Kummitment
    fields = [
        'task', 'kummitor', 
        'successactions', 'nextaction', 
        'possibleobstacles', 'minutesestimate', 
        'start', 'deadline', 'energytype', 
        'weekscheduled', 'dayscheduled', 
        'timescheduled', 'status', 'specific', 
        'measurable', 'achievable', 'relevant', 
        'timebound', 'healthy', 
        'wealthy', 'wise', 'connected', 
        'reflection', 'needhelp'
    ]
   
    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class KummitmentView(DetailView):
    model = Kummitment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class KummitmentList(FilterView):
    model = Kummitment
    filter_fields = ['kummitor', 'task', 'deadline', 'needhelp', 'status']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RoleView(DetailView):
    model = Role

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RoleList(FilterView):
    model = Role
    filter_fields = ['energizers', 'circle', 'project', 'rolestatus']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
