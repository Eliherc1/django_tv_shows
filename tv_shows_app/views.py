from django.shortcuts import render, redirect
from .models import *
from django.template import RequestContext, Template


def inicio(request):
    return redirect("/shows")

def shows(request):
    contexto={
        'shows' : Show.objects.all(),
    }
    return render(request, 'all_show.html', contexto)

def add_show(request):
    return render(request, 'add_show.html')


def crear_show(request):
    print(request.POST)

    show = Show.objects.create(
        title  = request.POST['show_title'],
        network  = request.POST['show_net'],
        release_date = request.POST['show_date'],
        description  = request.POST['show_desc'],
        
    )

    return redirect(f"/shows/{show.id}")

def ver_show(request,num):

    contexto={  'id': Show.objects.get(id=num).id ,
                'title': Show.objects.get(id=num).title ,
                'network': Show.objects.get(id=num).network ,
                'descripcion': Show.objects.get(id=num).description ,
                'rel_date': Show.objects.get(id=num).release_date ,
                'update': Show.objects.get(id=num).updated_at ,
    
    } 
    
    return render(request, 'ver_show.html', contexto)

def eliminar_show(request, num):
    show_obj = Show.objects.get(id=num)
    #print("-"*20, show_obj)
    show_obj.delete()

    return redirect("/shows")


def editar_show(request, num):
    if request.method == "GET" :
        formulario = {
            'edit_show': Show.objects.get(id=num) ,
        }

        return render(request, 'edit_show.html', formulario)

    if request.method == "POST" :

        print(request.POST)
        e= Show.objects.get(id=num)

        e.title  = request.POST['show_title_e']
        e.network  = request.POST['show_net_e']
        e.release_date = request.POST['show_date_e']
        e.description  = request.POST['show_desc_e']

        e.save()
        return redirect(f"/shows/{num}")


