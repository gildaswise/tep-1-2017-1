from django.core.files.images import get_image_dimensions
from django import forms


class FormPost(forms.Form):

    content = forms.CharField(max_length=256, required=True)
    image = forms.ImageField(required=False)

    def is_valid_from_form(self):
        return super(FormPost, self).is_valid()

    def clean_image(self):
        if 'image' in self.data and self.data['image'] is not '':
            image = self.data['image']
            try:
                main, sub = image.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'jpg', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, '
                                                'JPG or PNG image.')
            except AttributeError:
                pass
            return image
        else:
            return None