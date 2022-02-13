from django.db import models
from parks.models import Park, Trail

class Hiker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    registered = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Hike(models.Model):
    hiker_id = models.ForeignKey(Hiker, on_delete=models.CASCADE)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE)
    date = models.DateField()
    distance = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    notes = models.TextField(blank=True)
    trails = models.ManyToManyField(Trail)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['hiker_id', 'park_id', 'date'], name='unique_hike')]

    def __str__(self):
        return '%s %s %s' % (self.hiker_id.username, self.park_id.name, self.date)