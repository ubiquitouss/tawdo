# from django.shortcuts import render
# from django.utils import timezone
# from .models import Todo
# from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_protect
#
#
# # Create your views here.
# def home(request):
#     todo_items = Todo.objects.all().order_by("-added_date")
#     # -added_date means reverse way
#     return render(request, 'home/home.html', {
#         "todo_items": todo_items
#     })
#     print(todo_items)
#
#
# @csrf_protect
# def add_todo(request):
#     # print(request.POST)
#     current_date = timezone.now()
#     content = request.POST["content"]
#     created_obj = Todo.objects.create(added_date=current_date, text=content)
#     length_of_todos = Todo.objects.all().count()
#     return HttpResponseRedirect("/")
#
#
# @csrf_protect
# def delete_todo(request):
#     Todo.objects.get(id=todo_id).delete()
#     return HttpResponseRedirect("/")
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'home/home.html', {
      "todo_items": todo_items
    })

@csrf_exempt
def add_todo(request):
  current_date = timezone.now()
  content = request.POST["content"]
  created_obj = Todo.objects.create(added_date=current_date, text=content)
  return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")
