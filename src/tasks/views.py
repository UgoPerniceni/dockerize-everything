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
	return render(request, "tasks/task_update.html", context)

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
		"object": obj,
		"color": get_color(obj.color),
	}

	return render(request, "tasks/task_detail.html", context)

def task_close_view(request, id):
	obj = get_object_or_404(Task, id=id)
	if obj.status == 2:
		return redirect('/')
	if request.method == "POST":
		obj.close()
		obj.save()
		return redirect('/')
	context = {
		"object": obj
	}
	return render(request, "tasks/task_close.html", context)

def get_color(argument): 
    switcher = { 
        1: "bg-white", 
        2: "bg-light", 
        3: "bg-info text-white", 
       	4: "bg-warning text-white", 
        5: "bg-danger text-white", 
        6: "bg-success text-white", 
        7: "bg-primary text-white",
    } 
    return switcher.get(argument, '') 