from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import Post
from posts.forms import PostCreateForm, SearchForm
from django.contrib.auth.decorators import login_required

def main_view(request):
    return render(request, "components/navbar.html")
def about_me(request):
    if request.method == 'GET':
        return HttpResponse("I am a sigma male")
    else:
        pass

@login_required(login_url='/login/')
def about_my_friend(request):
    if request.method == 'GET':
        return render(request, 'about_my_friend.html')

@login_required(login_url='/login/')
def post_list_view(request):
    search_form = SearchForm()
    if request.method == 'GET':
        search = request.GET.get('search')
        category = int(request.GET.get('category')) if request.GET.get('category') else None
        ordering = request.GET.get('ordering')
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if category:
            posts = posts.filter(category_id=category)
        if ordering:
            posts = posts.order_by(ordering)
        limit = 2
        max_pages = posts.count()/ limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page -1 ) * limit
        end = start + limit

        posts = posts[start:end]

        context_data = {'posts': posts , "search_form": search_form , "max_pages": range(1, max_pages+1 ) }
        return render(request, 'posts/post_list.html', context = context_data,)
@login_required(login_url='/login/')
def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        return render(request, 'posts/post_detail.html', {'post': post})

@login_required(login_url='/login/')
def post_create_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        return render(request, 'posts/post_create.html', {'form': form})
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render (request, 'posts/post_create.html', {'form': form})
        elif form.is_valid():

            form.save()

            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')   juust form
            # image = form.cleaned_data.get('image')
            #
            # Post.objects.create(title=title, content=content, image=image)
            return redirect('/posts/')
