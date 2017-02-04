from django import forms

from .validators import validate_url


class URLForm(forms.Form):
    url = forms.CharField(label='Cut', validators=[validate_url])

    # We can validate our link this way:
    # def clean(self):
    #     cleaned_data = super(URLForm, self).clean()
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL!')
    #     return url
