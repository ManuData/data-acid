from django.shortcuts import get_object_or_404, render,redirect
from .models import Articles
from django.http import JsonResponse
from .forms import LeadsForm


# Create your views here.


def index(request):
    #articles = Articles.objects.all()[0]
    #return render(request,"blog/hello_world.html",{"data":articles})
    return render(request,"blog/hello_world.html")
    


def leads_form(request):
    if request.method == 'POST':
        form = LeadsForm(request.POST)
        if form.is_valid():
            # Process the form data (save to the database, send email, etc.)
            data_user = form.cleaned_data
            form_data = form.save(commit=False)
            form_data.save()
            return JsonResponse({'success': True,"userInput":data_user})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = LeadsForm()

    return render(request, 'blog/leads_form.html', {'form': form})
