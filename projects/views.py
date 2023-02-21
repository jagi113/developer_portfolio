from django.shortcuts import render, redirect
from projects.models import Tag, Project, Review
from projects.forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.utils import searchProjects, paginateProjects
from django.contrib import messages 
from django.db import IntegrityError

# Create your views here.


def index(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {"results": projects,
               "search_query": search_query,
               "custom_range": custom_range}
    return render(request, 'projects/projects.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    review_form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = project
        # Update project votecount
        
        
        if form.is_valid():
            try:
                messages.success(request, 'Your review was successfully saved!')
                review.save()
                project.getVoteCount
                pk = project.id
                return redirect("projects:project-detail", pk)
            except IntegrityError as e:
                messages.error(request, 'You already submitted your feedback.')
    context = {"project": project, "review_form":review_form}
    return render(request, 'projects/project-detail.html', context)


@ login_required(login_url='users:login')
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


@ login_required(login_url='users:login')
def update_project(request, pk):
    # for making sure that only owner of a project can update it we can either get his profile
    # and request project from his set based on id
    profile = request.user.profile
    project = profile.projects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects:project-detail", pk)
    else:
        context = {"project_form": form}
    return render(request, "projects/project-form.html", context)


@ login_required(login_url='users:login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if project.owner != request.user.profile:
        messages.error(
            request, "You are not authorized for deleting this post!")
        return redirect("projects:project-detail", pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")
