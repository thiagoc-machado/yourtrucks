from django.contrib import admin
from .models import Cars, Accessory, Photo, Video
from .forms import CarAdminForm
from django.template.loader import get_template
from django.utils.html import format_html


class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('carphoto_thumbnail', 'is_main', 'truck_photos') 
    readonly_fields = ('carphoto_thumbnail',)
    extra = 1

    def carphoto_thumbnail(self, instance):
        tpl = get_template("cardealer/admin/car_thumbnail.html")
        return format_html(
            '<input type="radio" name="main_photo" value="{}" {}> {}',
            instance.id,
            'checked' if instance.is_main else '',
            tpl.render({"photo": instance.car_photos}),
        )

    carphoto_thumbnail.short_description = ("Thumbnail")


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cars._meta.get_fields()]
    inlines = [PhotoInline, VideoInline]


    # form = CarAdminForm
    # inlines = [PhotoInline]
    # list_display = ['car_title', 'year', 'price', 'is_featured']
    # search_fields = ['car_title', 'year', 'price']

    # def save_related(self, request, form, formsets, change):
    #     super().save_related(request, form, formsets, change)
    #     form.save_photos(form.instance)


# from django.contrib import admin
# from .models import Car, Accessory
# from django.utils.html import format_html

# # Register your models here.

# class CarAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         if object.car_photos:
#             first_photo = object.car_photos.car_photo

#             print("tem foto")
#             return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(first_photo.photo.url))
#         else:
#             print("nao tem foto")
#             return "No Photo"

#     thumbnail.short_description = 'Car Image'
#     list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
#     list_display_links = ('id', 'thumbnail', 'car_title')
#     list_editable = ('is_featured',)
#     search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
#     list_filter = ('city', 'model', 'body_style', 'fuel_type')


# class AccessoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('id', 'name')

# admin.site.register(Accessory, AccessoryAdmin)
# admin.site.register(Car, CarAdmin)
