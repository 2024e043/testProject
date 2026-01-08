from django.shortcuts import render
from .models import Post 

def timeline(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }

    return render(request, 'timeline.html', context)

# Create your views here.
