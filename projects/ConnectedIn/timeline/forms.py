from django.core.files.images import get_image_dimensions
from django import forms


class FormPost(forms.Form):

    content = forms.CharField(max_length=256, required=True)
    image = forms.ImageField(required=False)

    def is_valid_from_form(self):
        return super(FormPost, self).is_valid()

    def clean_image(self):
        if 'image' in self.data and self.data['image'] is not '':

            avatar = self.data['image']

            try:
                w, h = get_image_dimensions(avatar)

                # validate dimensions
                max_width = max_height = 500
                if w > max_width or h > max_height:
                    raise forms.ValidationError(
                        u'Please use an image that is '
                        '%s x %s pixels or smaller.' % (max_width, max_height))

                # validate content type
                main, sub = avatar.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'jpg', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, '
                                                'JPG or PNG image.')

            except AttributeError:
                """
                Handles case when we are updating the user profile
                and do not supply a new avatar
                """
                pass

            return avatar
