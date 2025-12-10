from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='blog_images/')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title