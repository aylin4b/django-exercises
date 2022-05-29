from django.db import models

# Create your models here.
import imp
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Example(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)
    content = models.TextField()
    publishAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
