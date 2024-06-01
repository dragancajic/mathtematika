from django.http import HttpResponseRedirect
from django.shortcuts import render

from events.forms import CommentForm
from events.models import Post, Comment


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
        categories__name__contains=category
    ).order_by("-created_on")

    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "MathTEMATIKA/category.html", context)


# прикажи читав садржај поста -- све детаље
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()  # направи "празну" форму/образац за попуњавање :-)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "MathTEMATIKA/detail.html", context)
