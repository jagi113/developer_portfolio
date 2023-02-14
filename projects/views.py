from django.shortcuts import render, redirect
from projects.models import Tag, Project, Review
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    projects = Project.objects.all().order_by("-created_at")
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/project-detail.html', context)

@login_required(login_url='users:login')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            user = request.user        
            project.owner = user.profile
            project.save()
            pk = project.id
            return redirect("projects:project-detail", pk)
    else:
        context = {"project_form": ProjectForm()}
    return render(request, "projects/project-form.html", context)

@login_required(login_url='users:login')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    if project.owner != request.user.profile:
        messages.error(request, "You are not authorized for updating this post!")
        return redirect("projects:project-detail", pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects:project-detail", pk)
    else:
        context = {"project_form": form}
    return render(request, "projects/project-form.html", context)

@login_required(login_url='users:login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if project.owner != request.user.profile:
        messages.error(request, "You are not authorized for deleting this post!")
        return redirect("projects:project-detail", pk)
    if request.method=="POST":
        project.delete() 
        return redirect("projects:projects")