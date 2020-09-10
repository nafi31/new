from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Title, Item
from .forms import CreateList
from django.template import loader

def create(response):
    
    if response.method=="POST":
        form = CreateList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["title"]
            n = Title(name=name)
            content = form.cleaned_data["content"]
            c = Item(text=content,todolist=n)
            n.save()
            c.save()
            response.user.todo.add(n)
            
            form = CreateList()
        return HttpResponseRedirect("/notes/%i" %n.id)
    else:
        form = CreateList()
    return render(response, 'own/create.html', {"form":form})

def notes(response):
    return render(response,'own/notes.html',{})

def list(request,id):
    jk = Title.objects.get(id=id)
    tmpo= loader.get_template('own/x.html')
    context = {
        'jk': jk
        }
    return HttpResponse(tmpo.render(context,request))

