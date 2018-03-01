# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Posts
from .models import Authors
from .models import Categories
from .models import Comment
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):

    authors = Authors.objects.all()

    context = {
        "authors": authors
    }

    return render(request, "posts/index.html", context)

def blog(request, paginator_page):

    posts = Posts.objects.all().order_by("-created_at")
    categories = Categories.objects.all()
    authors = Authors.objects.all()
    search_text = ""

    if "category-q" in request.GET and request.GET["category-q"]:
        category_q = request.GET["category-q"]
        posts = Posts.objects.filter(category__name=category_q)

    if "author-q" in request.GET and request.GET["author-q"]:
        author_q = request.GET["author-q"]
        author_name_q = Q(author__name=author_q)
        posts = Posts.objects.filter(author_name_q)

    if "search-q" in request.GET and request.GET["search-q"]:
        search_text = request.GET["search-q"]
        search_q_words = search_text.split()
        for word in search_q_words:
            q = Q(title__icontains=word) | Q(category__name__icontains=word) | Q(author__name__icontains=word)
            posts = Posts.objects.filter(q)

    paginator = Paginator(posts, 2)
    paginator_current_page = paginator.page(paginator_page)
    posts = paginator_current_page.object_list
    num_pages = range(1, paginator.num_pages)

    context = {
        "posts": posts,
        "categories": categories,
        "authors": authors,
        "num_pages": num_pages,
        "paginator_selected_page": int(paginator_page),
        "search_text": search_text
    }

    return render(request, "posts/blog.html", context)

def story(request):
    return render(request, "posts/story.html")

def post(request, id):

    post = Posts.objects.get(id=id)
    post_comments = post.comments.all().order_by("-created_at")

    context = {
        "post": post,
        "post_comments": post_comments
    }

    return render(request, "posts/post.html", context)

def add(request):
    if request.method == "POST":

        if request.POST["commenter"] == "":
            commenter = "Unknown"
        else:
            commenter = request.POST["commenter"]
        comment_text = request.POST["comment-text"]
        post_id = request.POST["post-id"]

        current_post = Posts.objects.get(id=post_id)

        comment = Comment(text=comment_text, creator=commenter)

        comment.save()

        current_post.comments.add(comment)

        return redirect('/posts/post/' + post_id + "#post-comments")
    else:
        return render(request, 'posts/blog.html')

def addpost(request):
    return render(request, "posts/story.html")
