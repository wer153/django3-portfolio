from django.shortcuts import render, get_object_or_404

from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    total = len(blogs)
    return render(request, 'blog/all_blog.html', {'blogs': blogs, 'total':total})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.order_by('-date')

    blog_index = 0
    for index, current in enumerate(blogs):
        if current == blog:
            blog_index = index
            break

    next_index = min(blog_index+1,len(blogs)-1)
    prev_index = max(blog_index-1,0)

    prev = blogs[prev_index].id
    nxt = blogs[next_index].id

    second_next_index = min(next_index+1,len(blogs)-1)
    second_prev_index = max(prev_index-1,0)

    second_next = blogs[second_next_index].id
    second_prev = blogs[second_prev_index].id

    return render(request, 'blog/detail.html',
                  {'blog':blog,'id':blog_id, 'prev':prev, 'next':nxt, 'curr':blog_index+1,'next_index':next_index+1,
                   'prev_index':prev_index+1, 'second_next':second_next,'second_prev':second_prev,
                   'second_next_index':second_next_index+1, 'second_prev_index':second_prev_index+1})