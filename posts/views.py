from django.shortcuts import render

# Create your views here.
from posts.models import Post
from posts.forms import AddPost


def listview(request):
    posts = Post.objects.all()
    print(request.method)
    print(request.user)
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            Post.objects.create(title=title, content=content, author=request.user)

    form = AddPost()
    context = {"posts": posts, "form": form}
    return render(request, "posts/list.html", context)


def details(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        post.title = title
        post.content = content
        post.save()

    context = {"post": post}
    return render(request, "posts/details.html", context)
