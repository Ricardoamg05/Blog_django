from django.views.generic import TemplateView, ListView
from .models import Post

class homepageview(ListView):
    model= Post
    template_name="home.html"


class aboutpageview(TemplateView):
    template_name="about.html"

