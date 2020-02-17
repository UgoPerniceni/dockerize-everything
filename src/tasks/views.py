from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TaskModelForm
from .models import Task
import datetime

from django.views.generic import CreateView
from .models import Task

# Create your views here.

def home(request):
	queryset = Task.objects.all() # list of objects
	context = {
		"object_list": queryset
	}
	return render(request, 'home.html', context)

def task_create_view(request):
	form = TaskModelForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		task = Task(title=data['title'],
					description=data['description'],
					creation_date=datetime.datetime.now(),
					status=1,
					color=data['color'])
		task.save()
		return redirect("/")
	context = {
		'form': form
	}
	return render(request, "tasks/task_create.html", context)

def task_update_view(request, id=id):
	obj = get_object_or_404(Task, id=id)
	form = TaskModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("/")
	context = {
		'form': form
	}
	return render(request, "tasks/task_create.html", context)

def task_delete_view(request, id):
	obj = get_object_or_404(Task, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('/')
	context = {
		"object": obj
	}
	return render(request, "tasks/task_delete.html", context)

def task_detail_view(request, id):
	obj = get_object_or_404(Task, id=id)
	context = {
		"object": obj
	}
	return render(request, "tasks/task_detail.html", context)