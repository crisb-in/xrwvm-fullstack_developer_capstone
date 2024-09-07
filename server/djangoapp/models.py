from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed
    country = models.CharField(max_length=100, null=True, blank=True)
    establishment_year = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='car_make_logos/', null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model Model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CROSSOVER', 'Crossover'),
        ('SPORTSCAR', 'Sportscar'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    # Other fields as needed
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    transmission = models.CharField(
        max_length=10,
        choices=[('AUTO', 'Automatic'), ('MANUAL', 'Manual')],
        default='AUTO'
    )
    fuel_type = models.CharField(
        max_length=10,
        choices=[('GAS', 'Gasoline'), ('ELECTRIC', 'Electric')],
        default='GAS'
    )
    mileage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    color_options = models.CharField(max_length=100, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"  # Return the name as the string representation
