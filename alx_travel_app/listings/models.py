from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=255)  # Name of the listing
    description = models.TextField()          # Details about it
    location = models.CharField(max_length=255)  # Where it is
    price = models.DecimalField(max_digits=10, decimal_places=2)  # How much
    available = models.BooleanField(default=True)  # Can people still book it?
    created_at = models.DateTimeField(auto_now_add=True)  # When it was created

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')  # Linked listing
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=255)  # Who booked
    start_date = models.DateField()              # Start of booking
    end_date = models.DateField()                # End of booking
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} booking for {self.listing.title}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')  # Linked listing
    user_name = models.CharField(max_length=255)  # Reviewer name
    rating = models.IntegerField()                # Stars (1–5 usually)
    comment = models.TextField()                  # Their opinion
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} for {self.listing.title}"



class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for booking {self.booking.id} - {self.status}"
