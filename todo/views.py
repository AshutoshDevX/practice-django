from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Task
# Create your views here.


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html',{'tasks':tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title').strip()
        description = request.POST.get('description', '').strip()

        if title:
            Task.objects.create(title=title, description=description)
            return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_form.htmlxx')


def task_update(request,pk):
    task = get_object_or_404(Task, pk=pk)