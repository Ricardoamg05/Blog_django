from django.urls import path
from .views import homepageview, aboutpageview, BlogDetailView, BlogCreateView
urlpatterns=[
    path("",  homepageview.as_view(), name="home"),
    path("about/", aboutpageview.as_view(), name="about" ),
    path("post/<int:pk>/", BlogDetailView.as_view(), name= 'post_detail'),
    path("post/new", BlogCreateView.as_view(), name= "post_new")
]