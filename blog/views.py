from django.shortcuts import render
from django.http import HttpResponse,Http404

posts=[
    {
        'author' : 'sasidhar',
        'title' : 'blog+post1',
        'content' : 'First post content',
        'date_posted' : 'July 30 , 2020'
    },
 {
        'author' : 'bharath',
        'title' : 'blog+post2',
        'content' : 'second post content',
        'date_posted' : 'July 31, 2020'
    }

]

title = {
    'title': 'Django-blog'
}
def home(request):
    context = {  'posts' : posts  }
    return render(request,'blog/home.html',context)
def about(request):
    context = {'title':title}
    return render(request,'blog/about.html',context)
