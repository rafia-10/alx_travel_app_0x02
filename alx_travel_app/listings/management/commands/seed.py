from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Clear existing listings first (optional)
        Listing.objects.all().delete()

        sample_listings = [
            {
                "title": "Cozy Mountain Cabin",
                "description": "A peaceful cabin with a stunning mountain view.",
                "price": 120,
                "location": "Aspen, Colorado"
            },
            {
                "title": "Beachfront Bungalow",
                "description": "Wake up to the sound of waves in this lovely bungalow.",
                "price": 200,
                "location": "Miami, Florida"
            },
            {
                "title": "Urban Apartment",
                "description": "Modern apartment in the heart of the city.",
                "price": 150,
                "location": "New York, New York"
            }
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
