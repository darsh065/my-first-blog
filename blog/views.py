from django.shortcuts import render
from .models import Album

# Create your views here.

def post_list(request):
	albums = Album.objects.all()
	return render(request, 'blog/post_list.html', {'albums':albums})
    
