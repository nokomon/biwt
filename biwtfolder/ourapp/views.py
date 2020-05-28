from django.shortcuts import render, get_object_or_404
from biwtapp.models import Post
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone


def profile(request):
    return render(request, 'profile.html')

def music(request):
    posts = Post.objects
    user = User.objects
    return render(request, 'music.html', {'posts': posts})

def newpost(request):
    post = Post()
    post.title = request.POST['title']
    post.author = request.POST['author']
    post.body = request.POST['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('music')

def createpost(request):
    return render(request, 'createpost.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})