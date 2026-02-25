from django.db import models

class Accommodation(models.Model):
    host_id = models.IntegerField()

    title = models.CharField(max_length=255)
    description = models.TextField()

    location = models.JSONField()  # city, country, address

    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    guests = models.IntegerField()

    amenities = models.JSONField()  # wifi, parking, kitchen

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
