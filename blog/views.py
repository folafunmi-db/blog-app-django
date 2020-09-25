from django.shortcuts import render

# Create your views here.

# Using a class-based view
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# Using a function-based view
#
# def home(request):
#     return render(request, 'blog/home.html', {})