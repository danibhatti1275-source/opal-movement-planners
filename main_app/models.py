from django.db import models

class VendorCategory(models.Model):
    name = models.CharField(max_length=100)  # Photography, Decor, Catering
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    category = models.ForeignKey(VendorCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)           # e.g., "Subhan Studio"
    experience = models.CharField(max_length=100)      # e.g., "10+ Years"
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='vendor_photos/')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class EventPackage(models.Model):
    EVENT_TYPES = [
        ('bridal_shower', 'Bridal Shower'),
        ('mehndi', 'Mehndi'),
        ('barat', 'Barat'),
        ('walima', 'Walima'),
    ]
    
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    name = models.CharField(max_length=200)             # e.g., "Deal 1 (100 Persons)"
    image = models.ImageField(upload_to='package_images/', null=True, blank=True)
    with_catering_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    decor_only_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    persons = models.PositiveIntegerField(default=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_event_type_display()} - {self.name}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    event_type = models.CharField(max_length=50, choices=EventPackage.EVENT_TYPES)
    package = models.ForeignKey(EventPackage, on_delete=models.SET_NULL, null=True)
    event_date = models.DateField()
    guest_count = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.event_type}"

class ContactInfo(models.Model):
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.owner_name}: {self.phone}"