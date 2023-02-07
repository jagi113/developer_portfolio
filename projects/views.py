from django.shortcuts import render, redirect
from projects.models import Tag, Project, Review
from projects.forms import ProjectForm

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/project-detail.html', context)

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            pk = project.id
            return redirect("projects:project-detail", pk)
    else:
        context = {"project_form": ProjectForm()}
    return render(request, "projects/project-form.html", context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects:project-detail", pk)
    else:
        context = {"project_form": form}
    return render(request, "projects/project-form.html", context)

def delete_project(request, pk):
    if request.method=="POST":
        project = Project.objects.get(id=pk)
        project.delete() 
        return redirect("projects:projects")