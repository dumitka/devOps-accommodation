from django.db import models

class Accommodation(models.Model):
    host_id = models.IntegerField()

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.JSONField() 
    
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_guest = models.BooleanField(default=False)
    
    min_guests = models.IntegerField(default=1)
    max_guests = models.IntegerField(default=10)
    
    amenities = models.JSONField(default=list) # ["wifi", "parking"]
    images = models.JSONField(default=list) # ["url1", "url2"]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Availability(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='availabilities')
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.accommodation.title} ({self.from_date} - {self.to_date})"
