from django.db.models import Q
from users.models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, queryset, results):
    page = request.GET.get('page')    # current page we are on

    paginator = Paginator(queryset, results)

    try:
        # presenting only results of the requested page
        queryset = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        queryset = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        queryset = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex < 5:
        rightIndex = 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)
    return custom_range, queryset


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__name__icontains=search_query)
    )
    return profiles, search_query
