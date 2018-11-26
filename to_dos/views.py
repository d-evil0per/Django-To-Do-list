from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems
from django.http import JsonResponse
# Create your views here.


def index(request):
	all_items=TodoItems.objects.all()
	return render(request,"to-dos.html",{"items":all_items})

def addToDos(request):
	if request.POST['content']:
		newitem=TodoItems(content=request.POST['content'])
		newitem.save()
	return HttpResponseRedirect("/to-dos/")

def updateToDos(request):
	tid=request.POST['id']
	status=request.POST['status']
	item=TodoItems.objects.get(id=tid)
	item.status=status
	item.save()
	data = {}
	data['error_message'] = 'A user with this username already exists.'
	return JsonResponse(data)

def deleteToDos(request,tid):
	item=TodoItems.objects.get(id=tid)
	item.delete()
	return HttpResponseRedirect("/to-dos/")