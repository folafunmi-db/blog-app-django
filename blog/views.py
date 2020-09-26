from django.shortcuts import render

# Create your views here.

# Using a class-based view
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# Using a function-based view
#
# def home(request):
#     return render(request, 'blog/home.html', {})


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    # the context object name can be set to anything you want
    # here I set it to 'anything'
    context_object_name = "anything"
