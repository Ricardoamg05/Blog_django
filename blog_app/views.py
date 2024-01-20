from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView 
from .models import Post

class homepageview(ListView):
    model= Post
    template_name="home.html"


class aboutpageview(TemplateView):
    template_name="about.html"

class BlogDetailView(DetailView):
    model= Post
    template_name="post_detail.html"

class BlogCreateView(CreateView):
    model= Post
    template_name= "post_new.html"
    fields=["title", "author", "body"]

