from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Blog
# Create your views here.

class Blogsite(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

class BlogsiteDetail(DetailView):
    model = Blog
    template_name = 'detailview.html'
    context_object_name = 'blog'

class NewBlog(CreateView):
    model = Blog
    template_name = 'newblog.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class EditBlog(UpdateView):
    model = Blog
    template_name = 'editblog.html'
    fields = '__all__'

class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'deleteblog.html'
    success_url = reverse_lazy('home')

