from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Post, Comment, Category
from .forms import CommentForm, CustomUserCreationForm, CategoryForm, PostForm


def blog_index(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                author=request.user,
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
            )
            post.categories.set(form.cleaned_data["categories"])
            post.save()
            return redirect("index")

    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "blog/index.html", context)


def blog_categories(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_categoty = Category(name=form.cleaned_data["name"])
            new_categoty.save()
            return redirect("categories")
        
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "form": form
    }

    return render(request, "blog/categories.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/detail.html", context)


def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
    return render(request, "blog/register.html", {"form": form})
