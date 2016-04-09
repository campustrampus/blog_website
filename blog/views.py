from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
  blog_posts = Post.objects.order_by('-pub_date')[:10]
  context = {'blog_posts':blog_posts}
  return render(request,'blog/index.html', context)

def post_list(request):
  return render(request, 'blog/post_list.html', {})
