from django.contrib import admin
from .models import Car, Accessory, Photo, Video
from .forms import CarAdminForm
from django.utils.html import format_html


class AccessoryInline(admin.TabularInline):
    model = Car.accessories.through
    extra = 1

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('carphoto_thumbnail', 'is_main') 
    readonly_fields = ('carphoto_thumbnail',)
    extra = 0

    def carphoto_thumbnail(self, photo):
        if photo.truck_photos:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(photo.truck_photos.url))
        else:
            return "No Photo"

    carphoto_thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

class VideoInline(admin.TabularInline):
    model = Video
    extra = 0

class CarAdmin(admin.ModelAdmin):
    list_display = ['first_photo_thumbnail','id', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured']
    inlines = [PhotoInline, VideoInline ]
    form = CarAdminForm


    def first_photo_thumbnail(self, obj):
        first_photo = obj.get_main_photo()
        if first_photo:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(first_photo.truck_photos.url))
        else:
            return "No Photo"
    first_photo_thumbnail.short_description = 'Foto principal'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        form.save_photos(obj)

admin.site.register(Car, CarAdmin)
