from django.urls import path

from . import views

# The empty strings tells python to match
# all values and the URL is named 'home'
urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path(
        "post/<int:pk>/",
        views.BlogDetailView.as_view(),
        name="post_detail",
    ),
    path(
        "post/new/", views.BlogCreateView.as_view(), name="post_new"
    ),
]