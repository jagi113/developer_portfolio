from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def project_detail(request, pk):
    return HttpResponse(f"This is a {pk}. project detail")