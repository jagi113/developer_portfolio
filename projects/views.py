from django.shortcuts import render
from projects.models import Tag, Project, Review

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/project-detail.html', context) 