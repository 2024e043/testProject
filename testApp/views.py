from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# -----------------------------
# ホームページ（投稿フォーム & 投稿一覧）
# -----------------------------
def index(request):
    # フォーム送信時
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # 実験用なので author は設定せずに保存
            post.save()
            return redirect('index')
    else:
        form = PostForm()

    # 投稿一覧を新しい順に取得
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'form': form,
        'posts': posts,
    })

from rest_framework import generics
from .serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.select_related('author').order_by('-created_at')
    serializer_class = PostSerializer
