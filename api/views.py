from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProjectSerializer
from projects.models import Project

# return all the routes of our api
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'}, # api for voting only
        
        {'POST':'/api/users/token'}, # for a user to sign in
        {'POST':'/api/users/token/refresh'},
        
    ]
    return Response(routes)    

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)