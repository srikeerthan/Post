# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from InstaApp.models import Post, Like


def home(request):
    return render(request, 'registration/login.html')

@method_decorator(login_required,name='dispatch')
class PostsListView(ListView):
    model=Post

@method_decorator(login_required,name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields=['photo','caption']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
         return reverse_lazy('posts:myprofile')

@method_decorator(login_required,name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ['caption',]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:myprofile')

@method_decorator(login_required,name='dispatch')
class PostDeleteView(DeleteView):
    model=Post

    def get_object(self, queryset=None):
        post=Post.objects.get(id=self.kwargs.get("pk"))
        if post.author==self.request.user:
            return Post.objects.get(id=self.kwargs.get("pk"))
        else:
            raise Http404("you are not authenticated user")

    def get_success_url(self):
        return reverse_lazy('posts:userpost')

@login_required
def DeletePost(request,*args,**kwargs):
    post=Post.objects.get(id=kwargs['pk'])
    if post.author == request.user:
        post.delete()
    else:
        raise Http404("you are not authenticated user")

    return HttpResponseRedirect(
        reverse_lazy(
            'posts:myprofile'
        )
    )


@login_required
def like_post_view(request, *args, **kwargs):
    try:
        post = Post.objects.get(id=kwargs['pk'])

        _, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            like = Like.objects.get(
                post=kwargs['pk'],
                user=request.user
            )
            like.delete()
    except Post.DoesNotExist:
        messages.warning(
            request,
            'Post does not exist'
        )

    return HttpResponseRedirect(
                reverse_lazy(
                    'posts:list'
                )
    )

@method_decorator(login_required,name='dispatch')
class LikeListView(ListView):
    model=Like

    def get_queryset(self):
        return Like.objects.filter(post=self.kwargs['pk'])


@method_decorator(login_required,name='dispatch')
class UserPostView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    template_name = "InstaApp/UserPosts.html"
