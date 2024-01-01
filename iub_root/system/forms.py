from django import forms

from .models import Image_Data


class Image_Data_Form(forms.ModelForm):
    class Meta:
        model = Image_Data
        fields = "__all__"
