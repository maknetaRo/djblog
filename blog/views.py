from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.views import generic

from .models import Post
from .forms import PostForm

class PostDetailView(generic.DetailView):
    model = Post

class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 5
