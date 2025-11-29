from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')  # uploaded images stored in MEDIA_ROOT/recipes/
    time = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.title

