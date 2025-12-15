from django.db import models

# Create your models here.
#
class Post(models.Model):
    title = models.CharField(max_length=76)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    banner = models.ImageField(default='fallback.png',blank = True)
    
    def __str__(self):
        return self.title
