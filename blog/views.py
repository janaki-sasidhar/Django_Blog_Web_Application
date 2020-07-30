from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Post


title = {
    'title': 'Django-blog'
}
def home(request):
    context = {  'posts' : Post.objects.all().order_by('date_posted__minute').reverse()  }
    return render(request,'blog/home.html',context)
def about(request):
    context = {'title':title}
    return render(request,'blog/about.html',context)


