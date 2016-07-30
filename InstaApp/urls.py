"""InstaClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from InstaApp import views

urlpatterns = [
    url(r'^posts$',views.PostsListView.as_view(),name='list'),
    url(r'^create$',views.PostCreateView.as_view(),name='create'),
    url(r'posts/(?P<pk>[0-9]+)/update$',views.PostUpdateView.as_view(),name='update'),
    url(r'posts/(?P<pk>[0-9]+)/delete$',views.DeletePost),
    # url(r'posts/(?P<pk>[0-9]+)/delete$', views.PostDeleteView.as_view()),
    url(r'posts/(?P<pk>[0-9]+)/like$',views.like_post_view,name='like'),
    url(r'posts/(?P<pk>[0-9]+)/likesList$',views.LikeListView.as_view(),name='likesList'),
    url(r'myprofile$',views.UserPostView.as_view(),name='myprofile'),
]