from django.shortcuts import render, get_object_or_404
from .models import Group, Album, Song, GroupMember
from .forms import SearchForm

def index(request):
    """Главная страница с последними группами, альбомами и песнями."""
    
    query = request.GET.get('query', '')  # Получаем запрос от пользователя
    groups = albums = songs = []

    if query:
        groups = Group.objects.filter(name__icontains=query)
        albums = Album.objects.filter(name__icontains=query)
        songs = Song.objects.filter(name__icontains=query)
    else:
        groups = Group.objects.all()[:5]
        albums = Album.objects.all()[:5]
        songs = Song.objects.all()[:5]

    return render(request, 'wiki/index.html', {
        'query': query,
        'groups': groups,
        'albums': albums,
        'songs': songs,
    })

def group_detail(request, pk):
    """Детальная страница группы."""
    group = get_object_or_404(Group, pk=pk)
    albums = group.albums.all()
    songs = group.songs.all()
    members = group.members.all()
    return render(request, 'wiki/group_detail.html', {
        'group': group,
        'albums': albums,
        'songs': songs,
        'members': members,
    })

def album_detail(request, pk):
    """Детальная страница альбома."""
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all()
    return render(request, 'wiki/album_detail.html', {'album': album, 'songs': songs})

def song_detail(request, pk):
    """Детальная страница песни."""
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'wiki/song_detail.html', {'song': song})

def member_detail(request, pk):
    """Детальная страница участника группы."""
    member = get_object_or_404(GroupMember, pk=pk)
    return render(request, 'wiki/member_detail.html', {'member': member})

def search(request):
    """Поиск по группам, альбомам, песням и участникам."""
    query = request.GET.get('query', '')  
    groups = albums = songs = members = []
    
    if query:
        groups = Group.objects.filter(name__icontains=query)
        albums = Album.objects.filter(name__icontains=query)
        songs = Song.objects.filter(name__icontains=query)
        members = GroupMember.objects.filter(name__icontains=query)
    
    return render(request, 'wiki/search_results.html', {
        'query': query,
        'groups': groups,
        'albums': albums,
        'songs': songs,
        'members': members,
    })
