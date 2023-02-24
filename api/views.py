from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.serializers import ProjectSerializer
from projects.models import Project, Review


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    
    #This will create or get that object
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    
    # This will create or update that object
    review.value = data['value']
    review.body = data['body']
    review.save()
    project.getVoteCount
    
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)