from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from main.models import *

# Create your views here.
def index(request):
	return render(request,'owner/index.html',None)


def addpg(request):
	if(request.method=='GET'):
		return render(request,'owner/addpg.html',None)
	else:
		obj=pg()	
		obj.address=request.POST.get('address')
		obj.location=request.POST.get('location')
		obj.city=request.POST.get('city')
		obj.pin=request.POST.get('pin')
		obj.rent=request.POST.get('rent')
		obj.occupancy=request.POST.get('occupancy')
		obj.forgender=request.POST.get('gender')
		obj.size=request.POST.get('size')
		obj.rooms=request.POST.get('rooms')
		obj.intime='2018-08-10 08:00'
		obj.outtime='2018-08-10 23:00'
		obj.ownerid=owner.objects.get(id=1)
		obj.save()
		return HttpResponse('Record Saved')