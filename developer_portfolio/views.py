from django.shortcuts import redirect, render
from projects.models import Project

# general view for delete confirmation window passing what to delete, what delete view to move one, or on which url to get back


def delete_confirmation(request, type, pk):
    try:
        url = request.META.get('HTTP_REFERER')
    except:
        url = None
    if type == "Project":
        object = Project.objects.get(id=pk)
        path = 'projects:delete-project'
    context = {"object": object,
               "delete_path": path,
               "previous_url": url
               }
    return render(request, 'delete_window.html', context)
