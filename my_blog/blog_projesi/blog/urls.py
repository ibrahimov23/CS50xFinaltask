from unicodedata import name
from django.urls import path
from django.views import View
from blog.models import Parfume

from .views import (BlogListView, 
                    BlogDetailView, 
                    BlogCreateView, 
                    BlogUpdateView,
                    BlogDeleteView,
                    parfume,
                    )

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new", BlogCreateView.as_view(), name="post_yeni"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('', BlogListView.as_view(), name='home'),
    path('', parfume, name='home'),
    path('parfume/add/', Parfume, name='addParfume'),
    ]
