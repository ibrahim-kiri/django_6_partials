from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    A simple blog post model with title, content, author, and timestamps.
    This gives us real data to display using template partials.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at'] # Newest posts first

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """
    Comments on blog posts - we'll display these using partials too!
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __strt__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

