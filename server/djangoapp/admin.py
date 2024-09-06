from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'establishment_year')


# CarMakeAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ['type', 'year']
    search_fields = ['name']
    inlines = [CarModelInline]  # Display CarModelInline in CarMakeAdmin


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
