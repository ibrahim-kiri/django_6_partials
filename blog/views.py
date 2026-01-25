from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.
def post_list(request):
    """
    Display a list of all blog posts.
    THis view demostrates using partials for repeated post cards.
    """
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'page-title': 'All Blog Posts'
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    """
    Display a single post with its comments.
    This view demostrates using partials for both the post and comments.
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)
