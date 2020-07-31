from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


title = {
    'title': 'Django-blog'
}
def home(request):
    context = {  'posts' : Post.objects.all().order_by('date_posted__minute').reverse()  }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name="blog/home.html" #changing default template which would be blog/post_list.html
    context_object_name = 'posts'
    ordering=['-date_posted']

class UserPostListView(ListView):
    model = Post
    template_name="blog/user_posts.html" #changing default template which would be blog/post_list.html
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False


def about(request):
    context = {'title':title}
    return render(request,'blog/about.html',context)


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
    
