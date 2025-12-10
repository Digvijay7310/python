from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('others', 'Others'),
        ('life', "Life"),
        ('food', "Food"),
        ('fashions', 'Fashions'),
        ('travel', 'Travel'),
        ('bollywood', 'Bollywood'),
        ('cricket', 'Cricket'),
        ('others', 'Others'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    image = models.ImageField(upload_to='blog_images/')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title