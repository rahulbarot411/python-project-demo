from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    flower_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    work_description = models.TextField()
    work_image = models.ImageField(upload_to='artist_images/')

    def __str__(self):
        return self.name
    
    
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)  # Blog title
    content = models.TextField()  # Blog content
    author = models.CharField(max_length=100)  # Blog author
    image = models.ImageField(upload_to='blogs/')  # Image field (uploads images to 'blogs/' folder)
    published_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the blog was created
    slug = models.SlugField(unique=True)  # A URL-friendly version of the title
    
    def __str__(self):
        return self.title