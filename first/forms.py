from django import forms
from .models import Face_Image
import cv2
import numpy
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class ProcessedImageField(forms.FileField):
  def to_python(self, data):
    raw_content = super().to_python(data)
    if raw_content is None:
      return None

    content = raw_content.read()
    img_array = numpy.frombuffer(content, numpy.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    processed_content = cv2.imencode('.jpg', resized)[1].tobytes()

    # Create an InMemoryUploadedFile instance with processed content
    processed_file = InMemoryUploadedFile(
        file=BytesIO(processed_content),
        field_name=None,
        name='processed_img.jpg',
        content_type='image/jpeg',
        size=len(processed_content),
        charset=None
    )

    return processed_file

class ImageForm(forms.ModelForm):
    image = ProcessedImageField()

    class Meta:
        model = Face_Image
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def save(self, commit=True):
      processed_content = self.cleaned_data.get('image')

      
      face_image = Face_Image(image=processed_content)
      if commit:
        face_image.save()

      return face_image
