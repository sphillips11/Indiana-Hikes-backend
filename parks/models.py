from django.db import models
from django.utils.text import slugify

class Park(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.PositiveIntegerField()
    park_type = models.CharField(max_length=100)
    easy_trails = models.BooleanField(default=False)
    moderate_trails = models.BooleanField(default=False)
    rugged_trails = models.BooleanField(default=False)
    very_rugged_trails = models.BooleanField(default=False)
    accessibility = models.BooleanField()
    description = models.TextField()
    amenities = models.TextField()
    trail_map = models.FileField(upload_to='maps/')
    website = models.URLField()
    challenge = models.BooleanField()
    challenge_name = models.CharField(max_length=100, blank=True)
    challenge_description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    