from django.db import models
from datetime import datetime
from django.core.validators import URLValidator

    
class Car(models.Model):

    year_choice = [(r, r) for r in range(2000, (datetime.now().year + 1))]
    door_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
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
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )
    IS_FEATURED_CHOICES = (
        (False, 'No'),
        (True, 'Si'),
    )
    WARRANTY_CHOICES = (
        (False, 'No'),
        (True, 'Si'),
    )
    OWNERS_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 +'),
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
    BEDS_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    WEELS_CHOICES=(
        ('1', '4x2'),
        ('2', '4x4'),
        ('3', '4x6'),
        ('4', '4x8'),
        ('5', '4x10'),
        ('6', '4x12'),
    )

    # Basic
    is_featured = models.BooleanField(choices=IS_FEATURED_CHOICES, default=False, blank=True, null=True, verbose_name='Destacado')
    car_title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Título')
    year = models.IntegerField(choices=year_choice, blank=True, null=True, verbose_name='Año')
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name='Precio')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    availability = models.CharField(max_length=50, blank=True, null=True, verbose_name='Disponibilidad')
    delivery = models.CharField(max_length=50, blank=True, null=True, verbose_name='Entrega')
    documents = models.CharField(max_length=50, blank=True, null=True, verbose_name='Documentos')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ciudad')
    warranty = models.BooleanField(choices=WARRANTY_CHOICES, blank=True, null=True, verbose_name='Tiene garantía')
    guarantee = models.CharField(max_length=50, blank=True, null=True, verbose_name='Duración de la garantía')
    fuel_type = models.CharField(max_length=50, blank=True, null=True, choices=FUEL_TIPE_CHOICES, verbose_name='Combustible')
    no_of_owners = models.IntegerField(choices=OWNERS_CHOICE, blank=True, null=True, verbose_name='Propietarios')
    created_date = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name='Fecha de registro')
    passengers = models.IntegerField(choices=PASSENGERS_CHOICES, blank=True, null=True, verbose_name='Pasajeros')
    condition = models.CharField(max_length=100, blank=True, null=True, choices=CONDITION_CHOICES, verbose_name='Condición')
    obs = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    body_style = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estilo')
    Accessory = models.ManyToManyField('Accessory', blank=True, verbose_name='Accesorios')
    # slug = models.SlugField(max_length=1024)

    # Specifications
    ref = models.CharField(max_length=100, blank=True, null=True, verbose_name='Referencia')
    cabin = models.CharField(max_length=100, choices=CABIN_CHOICES, blank=True, null=True, verbose_name='Tipo de cabina')
    first_registration = models.DateField(blank=True, null=True, verbose_name='Primera matriculación')
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='Marca')
    driver_side = models.CharField(max_length=100, blank=True, null=True, choices=DRIVER_SIDE_CROICES, verbose_name='Lado del conductor')
    color = models.CharField(max_length=100, choices=COLOR_CHOICES, blank=True, null=True, verbose_name='Color exterior')
    color_int = models.CharField(max_length=100, choices=COLOR_CHOICES, blank=True, null=True, verbose_name='Color interior')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Modelo')
    kilometrage = models.CharField(max_length=100, blank=True, null=True, verbose_name='Kilometraje')

    # Technical specifications
    engine = models.CharField(max_length=100, blank=True, null=True, verbose_name='Motor')
    engine_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Tipo de motor')
    tacho = models.CharField(choices=TACHO_CHOICES, max_length=100, blank=True, null=True, verbose_name='Tacógrafo')
    width = models.CharField(max_length=100, blank=True, null=True, verbose_name='Anchura')
    length = models.CharField(max_length=100, blank=True, null=True, verbose_name='Longitud')
    fuel_capacity = models.CharField(max_length=100, blank=True, null=True, verbose_name='Capacidad de combustible')
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, max_length=100, blank=True, null=True, verbose_name='Transmisión')
    fifth_wheel_height = models.CharField(max_length=100, blank=True, null=True, verbose_name='Altura de la quinta rueda')
    qty_of_deposits = models.IntegerField(choices=QTY_DEPOSITS_CHOICES, blank=True, null=True, verbose_name='Cantidad de depósitos')
    qty_of_gears = models.IntegerField(choices=QTY_GEARS_CHOICES, blank=True, null=True, verbose_name='Cantidad de marchas')
    height = models.CharField(max_length=100, blank=True, null=True, verbose_name='Altura')

    # Axes and tires
    axis_distance = models.CharField(max_length=100, blank=True, null=True, verbose_name='Distancia entre ejes')
    axis_one_distance = models.CharField(max_length=100, blank=True, null=True, verbose_name='Distancia del eje uno')
    axis_one_breaks = models.CharField(max_length=100, blank=True, null=True, verbose_name='Frenos del eje uno')
    axis_one_suspension = models.CharField(choices=SUSPENSION_CHOICES, max_length=100, blank=True, null=True, verbose_name='Suspensión del eje uno')
    axis_one_weight = models.CharField(max_length=100, blank=True, null=True, verbose_name='Peso del eje uno')
    axis_one_percentage = models.CharField(choices=AXIS_PERCENTAGE_CHOICES, max_length=100, blank=True, null=True, verbose_name='Porcentaje del eje uno')
    axis_two_distance = models.CharField(max_length=100, blank=True, null=True, verbose_name='Distancia del eje dos')
    axis_two_breaks = models.CharField(max_length=100, blank=True, null=True, verbose_name='Frenos del eje dos')
    axis_two_suspension = models.CharField(choices=SUSPENSION_CHOICES, max_length=100, blank=True, null=True, verbose_name='Suspensión del eje dos')
    axis_two_weight = models.CharField(max_length=100, blank=True, null=True, verbose_name='Peso del eje dos')
    axis_two_percentage = models.CharField(choices=AXIS_PERCENTAGE_CHOICES, max_length=100, blank=True, null=True, verbose_name='Porcentaje del eje dos')
    front_tire = models.CharField(max_length=100, blank=True, null=True, verbose_name='Neumáticos delanteros')
    rear_tire = models.CharField(max_length=100, blank=True, null=True, verbose_name='Neumáticos detrás')
    weels = models.CharField(choices=WEELS_CHOICES, max_length=100, blank=True, null=True, verbose_name='Ruedas')
    beds = models.IntegerField(choices=BEDS_CHOICES, blank=True, null=True, verbose_name='Camas')


    # Features
    drive_train = models.CharField(choices=DRIVE_TRAIN_CHOICES, max_length=100, blank=True, null=True, verbose_name='Tipo de retarder')

    class Meta:
        verbose_name_plural = "Camiñones"
    
    def __str__(self):
        return self.car_title
    
    def get_main_photo(self):
        return self.truck_photos.filter(is_main=True).first() or self.truck_photos.first()

    def get_all_photos(self):
        return self.truck_photos.all()
    
class Accessory(models.Model):
    EXTRAS_CATEGORIES_CHOICES=(
        ('1', 'Seguridad'),
        ('2', 'Confort'),
        ('3', 'Calidad'),
        ('4', 'Servicios')
    )
    cars = models.ManyToManyField('Car', related_name='accessories')
    name = models.CharField(max_length=100)
    extras_categories = models.CharField(max_length=100, choices=EXTRAS_CATEGORIES_CHOICES)

    class Meta:
        verbose_name_plural = "Accesorios"
    
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    truck = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='truck_photos', blank=True, null=True)
    truck_photos = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Imágenes"

    def __str__(self):
        return self.truck_photos.url

class Video(models.Model):
    truck = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='truck_videos', blank=True, null=True)
    youtube_link = models.CharField(max_length=200, validators=[URLValidator()], blank=True, null=True)

    class Meta:
        verbose_name_plural = "Vídeos"

    def __str__(self):
        return self.youtube_link
    





# from django.db import models
# from datetime import datetime
# from ckeditor.fields import RichTextField
# from multiselectfield import MultiSelectField

# # Create your models here.
# class Car(models.Model):

#     state_choice = (
#         ('AL', 'Alabama'),
#         ('AK', 'Alaska'),
#         ('AZ', 'Arizona'),
#         ('AR', 'Arkansas'),
#         ('CA', 'California'),
#         ('CO', 'Colorado'),
#         ('CT', 'Connecticut'),
#         ('DE', 'Delaware'),
#         ('DC', 'District Of Columbia'),
#         ('FL', 'Florida'),
#         ('GA', 'Georgia'),
#         ('HI', 'Hawaii'),
#         ('ID', 'Idaho'),
#         ('IL', 'Illinois'),
#         ('IN', 'Indiana'),
#         ('IA', 'Iowa'),
#         ('KS', 'Kansas'),
#         ('KY', 'Kentucky'),
#         ('LA', 'Louisiana'),
#         ('ME', 'Maine'),
#         ('MD', 'Maryland'),
#         ('MA', 'Massachusetts'),
#         ('MI', 'Michigan'),
#         ('MN', 'Minnesota'),
#         ('MS', 'Mississippi'),
#         ('MO', 'Missouri'),
#         ('MT', 'Montana'),
#         ('NE', 'Nebraska'),
#         ('NV', 'Nevada'),
#         ('NH', 'New Hampshire'),
#         ('NJ', 'New Jersey'),
#         ('NM', 'New Mexico'),
#         ('NY', 'New York'),
#         ('NC', 'North Carolina'),
#         ('ND', 'North Dakota'),
#         ('OH', 'Ohio'),
#         ('OK', 'Oklahoma'),
#         ('OR', 'Oregon'),
#         ('PA', 'Pennsylvania'),
#         ('RI', 'Rhode Island'),
#         ('SC', 'South Carolina'),
#         ('SD', 'South Dakota'),
#         ('TN', 'Tennessee'),
#         ('TX', 'Texas'),
#         ('UT', 'Utah'),
#         ('VT', 'Vermont'),
#         ('VA', 'Virginia'),
#         ('WA', 'Washington'),
#         ('WV', 'West Virginia'),
#         ('WI', 'Wisconsin'),
#         ('WY', 'Wyoming'),
#     )

#     year_choice = []
#     for r in range(2000, (datetime.now().year+1)):
#         year_choice.append((r,r))

#     features_choices = (
#         ('Cruise Control', 'Cruise Control'),
#         ('Audio Interface', 'Audio Interface'),
#         ('Airbags', 'Airbags'),
#         ('Air Conditioning', 'Air Conditioning'),
#         ('Seat Heating', 'Seat Heating'),
#         ('Alarm System', 'Alarm System'),
#         ('ParkAssist', 'ParkAssist'),
#         ('Power Steering', 'Power Steering'),
#         ('Reversing Camera', 'Reversing Camera'),
#         ('Direct Fuel Injection', 'Direct Fuel Injection'),
#         ('Auto Start/Stop', 'Auto Start/Stop'),
#         ('Wind Deflector', 'Wind Deflector'),
#         ('Bluetooth Handset', 'Bluetooth Handset'),
#     )

#     door_choices = (
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#         ('6', '6'),
#     )

#     car_title = models.CharField(max_length=255)
#     state = models.CharField(choices=state_choice, max_length=100)
#     city = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     year = models.IntegerField(('year'), choices=year_choice)
#     condition = models.CharField(max_length=100)
#     price = models.IntegerField()
#     description = RichTextField()
#     car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     features = MultiSelectField(choices=features_choices)
#     body_style = models.CharField(max_length=100)
#     engine = models.CharField(max_length=100)
#     transmission = models.CharField(max_length=100)
#     interior = models.CharField(max_length=100)
#     miles = models.IntegerField()
#     doors = models.CharField(choices=door_choices, max_length=10)
#     passengers = models.IntegerField()
#     vin_no = models.CharField(max_length=100)
#     milage = models.IntegerField()
#     fuel_type = models.CharField(max_length=50)
#     no_of_owners = models.CharField(max_length=100)
#     is_featured = models.BooleanField(default=False)
#     created_date = models.DateTimeField(default=datetime.now, blank=True)

#     def __str__(self):
#         return self.car_title
