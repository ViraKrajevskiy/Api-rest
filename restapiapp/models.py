from django.db import models
from django.utils.text import slugify

class Actors(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateTimeField()

    def actor_save(self,*args,**kwargs):
        if not 

class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)
    year = models.IntegerField(default=1920)
    actors = models.ManyToManyField(Actors, related_name='actors')
    genre = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)
            slug = original_slug
            count = 1
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
