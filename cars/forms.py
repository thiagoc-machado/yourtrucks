from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _

from .models import Car, Photo

class CarAdminForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    photos = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photo"):
            validate_image_file_extension(upload)

def save_photos(self, car):
    """Process each uploaded image."""
    for upload in self.files.getlist("photos"):
        photo_instance = Photo(truck=car, truck_photos=upload)
        photo_instance.save()
