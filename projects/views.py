from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'projects/projects.html')

def project_detail(request, pk):
    return render(request, 'projects/project-detail.html', {"message":f"This is a {pk}. project detail", "slug": pk})