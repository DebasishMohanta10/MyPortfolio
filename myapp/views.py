from django.shortcuts import render
from .models import Project
# Create your views here.
from .forms import ContactForm
def home(request):
    projects = Project.objects.all()

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
        
    context = {"projects": projects , "form": form} 
    return render(request,"index.html",context)

def show_project(request,pk = None):
    if pk:
        project = Project.objects.get(pk=pk)
    else:
        project = ""
    return render(request,"show_project.html",{"project": project}) 
