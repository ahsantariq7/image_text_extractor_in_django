from django.urls import path

from .views import Image_data_Show, Image_Data_View

urlpatterns = [
    path("", Image_Data_View.as_view()),
    path("success/", Image_data_Show.as_view()),
]
