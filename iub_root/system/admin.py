from django.contrib import admin

from .models import Image_Data


# Register your models here.
@admin.register(Image_Data)
class Image_Data_Admin(admin.ModelAdmin):
    list_display = ["id"]
