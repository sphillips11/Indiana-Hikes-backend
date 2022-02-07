from django.db import models
from django.urls import reverse

class Park(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="IN")
    zip = models.PositiveIntegerField()
    phone = models.CharField(max_length=14)
    park_type = models.CharField(max_length=100, default="Indiana State Park")
    accessible_trails = models.BooleanField(default=False)
    easy_trails = models.BooleanField(default=False)
    moderate_trails = models.BooleanField(default=False)
    difficult_trails = models.BooleanField(default=False)
    more_difficult_trails = models.BooleanField(default=False)
    moderately_rugged = models.BooleanField(default=False)
    rugged_trails = models.BooleanField(default=False)
    very_rugged_trails = models.BooleanField(default=False)
    accessibility = models.BooleanField()
    description = models.TextField()
    amenities = models.TextField()
    trail_map = models.URLField()
    website = models.URLField()
    challenge = models.BooleanField()
    challenge_name = models.CharField(max_length=100, blank=True)
    challenge_description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('park_detail', kwargs={'slug': self.slug})

class Trail (models.Model):
    name = models.CharField(max_length=100)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE)
    distance = models.CharField(max_length=7, blank=True)
    rating = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    accessible = models.BooleanField(default=False)

    def __str__(self):
        return self.name (self.park_id)