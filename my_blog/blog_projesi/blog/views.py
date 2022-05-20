
from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Parfume
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AddParfumeForm
# Create your views here.

# class Blogview(ListView):
#     model=Post
#     template_name='product1.html'


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_yeni.html"
    fields = "__all__"
    reverse_lazy("home")


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def parfume(request):
    form = Parfume()
    objects = Parfume.objects.all()
    context = {
        "form": form,
        "objects_list": objects
    }
    return render(request, 'index.html', context)

def post(request):
    form = Post()
    objects = Post.objects.all()
    context = {
        "form": form,
        "posts": objects
    }
    return render(request, 'index.html', context)


class HomeView(ListView):
    model = Parfume
    template_name = 'index.html'
