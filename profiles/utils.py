from django.db.models import Q
from .models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profiles = Profile.objects.distinct().filter(
        Q(username__icontains=search_query) |
        Q(location__icontains=search_query)
    ).exclude(
        Q(username__isnull=True)
    ).order_by('username')

    return profiles, search_query
