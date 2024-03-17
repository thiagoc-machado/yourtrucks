from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from .models import Cars, Photo

class CarAdminForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ('title', 'slug')

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, Cars):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = Photo(Cars=Cars, Cars_photos=upload)
            photo.save()
