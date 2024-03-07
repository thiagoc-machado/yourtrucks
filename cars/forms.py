from django import forms
from django.core.validators import validate_image_file_extension
from .models import Car, Photo

class CarAdminForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, car):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = Photo(car=car, car_photos=upload)
            photo.save()
