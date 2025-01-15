from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def about_me(request):
    return HttpResponse("I am a sigma male")

def about_my_friend(request):
    return render(request, 'about_my_friend.html')

def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        return render(request, 'posts/post_detail.html', {'post': post})
