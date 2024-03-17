from django.db import models
from datetime import datetime
from django.core.validators import URLValidator

    
class Accessory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Cars(models.Model):

    year_choice = [(r, r) for r in range(2000, (datetime.now().year + 1))]
    door_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
    )

    QTY_DEPOSITS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    # qty_of_gears
    QTY_GEARS_CHOICES = (
        (5, '5'),
        (6, '6'),
        (8, '8'),
        (10, '10'),
        (12, '12'),
    )
    TRANSMISSION_CHOICES = (
        ('1', 'Automatico'),
        ('2', 'Manual'),
        ('3', 'Semi-automatico'),
        ('4', 'Semi-manual'),
        ('5', 'Mecanico'),
        ('6', 'Semi-mecanico'),
        ('7', 'Mecanico-automatico'),
        ('8', 'Mecanico-semi-automatico'),
        ('9', 'Mecanico-semi-manual'),
    )
    TACHO_CHOICES = (
        ('1', 'Digital'),
        ('2', 'Disco'),
    )
    SUSPENSION_CHOICES = (
        ('1', 'Parabolica'),
        ('2', 'Neumática'),
        ('3', 'Muelles'),
        ('4', 'Pneumática'),
        ('5', 'Ballestas'),
        ('6', 'Eje rígido'),
    )
    AXIS_PERCENTAGE_CHOICES = (
        ('1', '10 %'),
        ('2', '20 %'),
        ('3', '30 %'),
        ('4', '40 %'),
        ('5', '50 %'),
        ('6', '60 %'),
        ('7', '70 %'),
        ('8', '80 %'),
        ('9', '90 %'),
    )
    DRIVE_TRAIN_CHOICES = (
        ('1', 'hidráulico'),
        ('2', 'eléctrico'),
        ('3', 'hidrodinámico'),
        ('4', 'electromagnético'),
        ('5', 'neumático'),
        )
    PASSENGERS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    IS_FEATURED_CHOICES = (
        ('1', 'No'),
        ('2', 'Si'),
    )
    WARRANTY_CHOICES = (
        ('1', 'No'),
        ('2', 'Si'),
    )
    OWNERS_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5 +'),
    )
    FUEL_TIPE_CHOICES = (
        ('1', 'Diesel'),
        ('2', 'Gasolina'),
        ('3', 'Gas'),
        ('4', 'Hibrido'),
        ('5', 'Electrico'),
        ('6', 'Bio'),
    )
    CONDITION_CHOICES = (
        ('1', 'Nuevo'),
        ('2', 'Usado'),
        ('3', 'Usado, como nuevo'),
    )
    CABIN_CHOICES = (
        ('1', 'Cabina Normal'),
        ('2', 'Cabina con Litera'),
        ('3', 'Cabina Alta'),    
        ('4', 'Cabina Baja'),
        ('5', 'Cabina Extra-Ancha'),
        ('6', 'Cabina Confort'),
        ('7', 'Cabina Dormitorio'),
        ('8', 'Cabina Doble'),
        ('9', 'Cabina Corta'),
        ('10', 'Cabina Modular'),
        )
    DRIVER_SIDE_CROICES = (
        ('1', 'Izquierda'),
        ('12', 'Derecha'),
    )

    COLOR_CHOICES=(
        ('1', 'Blanco'),
        ('2', 'Negro'),
        ('3', 'Gris'),
        ('4', 'Rojo'),
        ('5', 'Amarillo'),
        ('6', 'Verde'),
        ('7', 'Azul'),
        ('8', 'Naranja'),
        ('9', 'Rosa'),
        ('10', 'Marrón'),
        ('11', 'Plata'),
    )


    # Basic
    is_featured = models.BooleanField(choices = IS_FEATURED_CHOICES, default=False, blank=True, null=True, verbose_name='Favorito')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Titulo') 
    year = models.IntegerField(choices=year_choice, blank=True, null=True, verbose_name='Año')
    price = models.IntegerField(blank=True, null=True, verbose_name='Precio')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    availability = models.CharField(max_length=50, blank=True, null=True, verbose_name='Disponibilidad')
    delivery = models.CharField(max_length=50, blank=True, null=True, verbose_name='Entrega')
    documents = models.CharField(max_length=50, blank=True, null=True, verbose_name='Documentos')
    location = models.CharField(max_length=50, blank=True, null=True, verbose_name='Umbicación')
    warranty = models.BooleanField(choices=WARRANTY_CHOICES, blank=True, null=True, verbose_name='Tiene garantia')
    guarantee = models.CharField(max_length=50, blank=True, null=True, verbose_name='Tiempo de garantia')
    fuel_type = models.CharField(max_length=50, blank=True, null=True, choices = FUEL_TIPE_CHOICES, verbose_name='Combustible')
    no_of_owners = models.IntegerField(choices = OWNERS_CHOICE, blank=True, null=True, verbose_name='Proprietarios')
    created_date = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name='Fecha de cadastro')
    passengers = models.IntegerField(choices = PASSENGERS_CHOICES, blank=True, null=True, verbose_name='Passageros')
    condition = models.CharField(max_length=100, blank=True, null=True,choices=CONDITION_CHOICES, verbose_name='Condición')
    obs = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    slug = models.SlugField(max_length=1024)
    
    # Specifications
    ref = models.CharField(max_length=100, blank=True, null=True, verbose_name='Referencia')
    cabin = models.CharField(max_length=100,choices=CABIN_CHOICES, blank=True, null=True, verbose_name='Tipo de cabina')
    first_registration = models.DateField(blank=True, null=True, verbose_name='Primera matricula')
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fabricante')
    driver_side = models.CharField(max_length=100, blank=True, null=True,choices=DRIVER_SIDE_CROICES, verbose_name='Lado del conductor')
    color_ext = models.CharField(max_length=100,choices=COLOR_CHOICES, blank=True, null=True, verbose_name='Color externo')
    color_int = models.CharField(max_length=100, choices=COLOR_CHOICES, blank=True, null=True, verbose_name='Color interno')
    model = models.CharField(max_length=100, blank=True, null=True) # tipo do caminhao
    kilometrage = models.CharField(max_length=100, blank=True, null=True)
    
    # Technical specifications
    engine = models.CharField(max_length=100, blank=True, null=True)
    engine_type = models.CharField(max_length=100, blank=True, null=True)
    tacho = models.CharField(choices=TACHO_CHOICES, max_length=100, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    fuel_capacity = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(choices = TRANSMISSION_CHOICES, max_length=100, blank=True, null=True)
    fifth_wheel_height = models.CharField(max_length=100, blank=True, null=True)
    qty_of_deposits = models.IntegerField(choices=QTY_DEPOSITS_CHOICES, blank=True, null=True)
    qty_of_gears = models.IntegerField(choices=QTY_GEARS_CHOICES, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    
    # Axes and tires
    axis_distance = models.CharField(max_length=100, blank=True, null=True) # Between axes
    axis_one_distance = models.CharField(max_length=100, blank=True, null=True) 
    axis_one_breaks = models.CharField(max_length=100, blank=True, null=True) 
    axis_one_suspension = models.CharField(choices=SUSPENSION_CHOICES, max_length=100, blank=True, null=True)
    axis_one_weight = models.CharField(max_length=100, blank=True, null=True)
    axis_one_percentage = models.CharField(choices = AXIS_PERCENTAGE_CHOICES, max_length=100, blank=True, null=True)
    axis_two_distance = models.CharField(max_length=100, blank=True, null=True) 
    axis_two_breaks = models.CharField(max_length=100, blank=True, null=True) 
    axis_two_suspension = models.CharField(choices=SUSPENSION_CHOICES, max_length=100, blank=True, null=True) 
    axis_two_weight = models.CharField(max_length=100, blank=True, null=True) 
    axis_two_percentage = models.CharField(choices = AXIS_PERCENTAGE_CHOICES, max_length=100, blank=True, null=True)
    
    # Features
    drive_train = models.CharField(choices = DRIVE_TRAIN_CHOICES, max_length=100, blank=True, null=True) # Retarder
    
    def __str__(self):
        return self.title
    
    def get_main_photo(self):
        return self.truck_photos.filter(is_main=True).first() or self.truck_photos.first()

    def get_all_photos(self):
        return self.truck_photos.all()
    

class Intern_cabin(models.Model):
    intern_extras = models.ManyToManyField(Accessory, blank=True)

    def __str__(self):
        return self.intern_extras.name


class Ext_extras(models.Model):
    ext_extras = models.ManyToManyField(Accessory, blank=True)

    def __str__(self):
        return self.ext_extras.name
    

class Extras_security(models.Model):
    extras_security = models.ManyToManyField(Accessory, blank=True)

    def __str__(self):
        return self.extras_security.name
    

class Photo(models.Model):
    truck = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='truck_photos', blank=True, null=True)
    truck_photos = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.truck_photos.url

class Video(models.Model):
    truck = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='truck_videos', blank=True, null=True)
    youtube_link = models.CharField(max_length=200, validators=[URLValidator()], blank=True, null=True)

    def __str__(self):
        return self.youtube_link



# car_title = models.CharField(max_length=255)
    # state = models.CharField(max_length=100, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # color = models.CharField(max_length=100, blank=True, null=True)
    # model = models.CharField(max_length=100, blank=True, null=True)
    # year = models.IntegerField(('year'), choices=year_choice, blank=True, null=True)
    # condition = models.CharField(max_length=100, blank=True, null=True)
    # price = models.IntegerField(blank=True, null=True)
    # description = RichTextField(blank=True, null=True)
    # features = MultiSelectField(choices=[(accessory.id, accessory.name) for accessory in Accessory.objects.all()], blank=True, null=True)
    # body_style = models.CharField(max_length=100, blank=True, null=True)
    # engine = models.CharField(max_length=100, blank=True, null=True)
    # transmission = models.CharField(max_length=100, blank=True, null=True)
    # interior = models.CharField(max_length=100, blank=True, null=True)
    # miles = models.IntegerField(blank=True, null=True)
    # doors = models.CharField(choices=door_choices, max_length=10, blank=True, null=True)
    # passengers = models.IntegerField(blank=True, null=True)
    # vin_no = models.CharField(max_length=100, blank=True, null=True)
    # milage = models.IntegerField(blank=True, null=True)
    # fuel_type = models.CharField(max_length=50, blank=True, null=True)
    # no_of_owners = models.CharField(max_length=100, blank=True, null=True)
    # is_featured = models.BooleanField(default=False, blank=True, null=True)
    # created_date = models.DateTimeField(default=datetime.now, blank=True, null=True)



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