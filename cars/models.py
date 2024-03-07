from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

    
class Accessory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(('year'), choices=year_choice, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    features = MultiSelectField(choices=[(accessory.id, accessory.name) for accessory in Accessory.objects.all()], blank=True, null=True)
    body_style = models.CharField(max_length=100, blank=True, null=True)
    engine = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    interior = models.CharField(max_length=100, blank=True, null=True)
    miles = models.IntegerField(blank=True, null=True)
    doors = models.CharField(choices=door_choices, max_length=10, blank=True, null=True)
    passengers = models.IntegerField(blank=True, null=True)
    vin_no = models.CharField(max_length=100, blank=True, null=True)
    milage = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    no_of_owners = models.CharField(max_length=100, blank=True, null=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.car_title
    
    def get_main_photo(self):
        return self.car_photos.filter(is_main=True).first() or self.car_photos.first()

    def get_all_photos(self):
        return self.car_photos.all()
    
class Photo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_photos', blank=True, null=True)
    car_photos = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.car_photos.url



  # features_choices = (
    #     ('Cruise Control', 'Cruise Control'),
    #     ('Audio Interface', 'Audio Interface'),
    #     ('Airbags', 'Airbags'),
    #     ('Air Conditioning', 'Air Conditioning'),
    #     ('Seat Heating', 'Seat Heating'),
    #     ('Alarm System', 'Alarm System'),
    #     ('ParkAssist', 'ParkAssist'),
    #     ('Power Steering', 'Power Steering'),
    #     ('Reversing Camera', 'Reversing Camera'),
    #     ('Direct Fuel Injection', 'Direct Fuel Injection'),
    #     ('Auto Start/Stop', 'Auto Start/Stop'),
    #     ('Wind Deflector', 'Wind Deflector'),
    #     ('Bluetooth Handset', 'Bluetooth Handset'),
    # )