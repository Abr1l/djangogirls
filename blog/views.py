from django.shortcuts import render
from django.utils import timezone
from .models import Post 
#el punto despues de models indica que es el directorio o aplicación actual

# Como views.py y models.py están en el mismo directorio, simplemente #usamos . y el nombre del archivo (sin .py). Ahora importamos el nombre del #modelo (Post). '''

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(publisher_date__lte=timezone.now()).order_by('publisher_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


