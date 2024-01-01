import cv2
import numpy as np
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from pytesseract import *

from .forms import Image_Data_Form
from .models import Image_Data


# Create your views here.
class Image_Data_View(CreateView):
    form_class = Image_Data_Form
    template_name = "image.html"
    queryset = Image_Data.objects.all()
    success_url = "success/"

    def form_valid(self, form):
        image = form.cleaned_data["image"]
        # = str(image)
        image_file = image

        # Read the image using OpenCV
        image_data = image_file.read()
        nparr = np.fromstring(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Perform OCR using pytesseract
        self.text = pytesseract.image_to_string(gray, lang="eng")

        # Now 'text' contains the extracted text from the image
        self.request.session["extracted_text"] = self.text
        print("Extracted Text:")

        return super().form_valid(form)


class Image_data_Show(TemplateView):
    template_name = "show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = self.request.session.get("extracted_text", None)

        return context
