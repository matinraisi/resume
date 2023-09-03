from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkCV
# Create your views here.
def homeview(request):
   qury = WorkCV.objects.all()
   context = {
      'qury' : qury
   }
   return render(request , 'home/index.html',context)



def GetData(request):
   qury = WorkCV.objects.all()
   context = {
      'qury' : qury
   }

   return render(request , 'home/data.html' , context)
