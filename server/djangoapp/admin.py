from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'establishment_year')  # Ensure fields exist in CarModel

# CarMakeAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'year']  # Ensure fields exist in CarMake
    list_filter = ['type', 'year']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
