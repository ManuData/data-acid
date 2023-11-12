from django.shortcuts import get_object_or_404, render
from .models import Articles



# Create your views here.


def index(request):
    #articles = Articles.objects.all()[0]
    #return render(request,"blog/hello_world.html",{"data":articles})
    return render(request,"blog/hello_world.html")
    
 