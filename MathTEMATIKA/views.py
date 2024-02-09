from django.shortcuts import render
from MathTEMATIKA.models import Post, Comment

# Create your views here.

# излистај све постове
def blog_index(request):
    # `-` уреди у опадајућем поретку, од најновијег поста!
    posts = Post.objects.all().order_by("-created_on")

    context = {
        "posts": posts,
    }
    return render(request, "MathTEMATIKA/index.html", context)


# излистај све постове за одређену категорију
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__names__contains = category
    ).order_by("-created_on")

    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "MathTEMATIKA/category.html", context)


# прикажи читав садржај поста -- све детаље
def blog_detail(request, pk):
    post = Post.objects.get(pk = pk)
    comments = Comment.objects.filter(post = post)

    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "MathTEMATIKA/detail.html", context)
