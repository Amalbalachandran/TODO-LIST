from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from.models import ToDo
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):

    todo = ToDo.objects.all()
    return render(request,'home.html',{'todo':todo})


def insert(request):
        if request.method == 'POST':
            task = request.POST['task']
            date = request.POST['date']
            time = request.POST['time']
       
            todo = ToDo(Task=task,Date=date,Time=time)
            todo.save()
            print (todo)
            return redirect('fapp:home')
        return render(request, 'insert.html')


def edit(request,todo_id):
     todo = ToDo.objects.all()
     sel_todo =ToDo.objects.get(id = todo_id)
     context={'todo':todo,'sel_todo': sel_todo,'todo_id':todo_id}
     print(todo_id)
     print(sel_todo)
     return render(request,'insert.html',context)


def update(request,todo_id):
     todo = ToDo.objects.get(id=todo_id)
     todo.Task = request.POST['task']
     todo.Date = request.POST['date']
     todo.Time = request.POST['time']
     todo.save()
     # return redirect('fapp:insert',{'todo_id':todo_id})
     return redirect('fapp:home')

def insert_task(request):
     todo= ToDo.objects.all()
     context={'todo':todo}
     return render(request,'insert.html',context)

def delete(request, id):
    task = ToDo.objects.get(id=id)
    task.delete()
    return redirect('fapp:home')
     
