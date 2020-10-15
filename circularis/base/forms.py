from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from django.forms import ModelForm

from circularis.base.common import get_latitude_longitude
from circularis.base.models import Address


class CreateAddress(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'unit', 'city', 'province', 'postal_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(PrependedText('street', "", placeholder="eg.: 123 Main St"),
                       css_class='form-group col-md-8 mb-0'),
                Column(PrependedText('unit', "", placeholder="eg.: 202 (or leave it blank if it is a house)"),
                       css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column(PrependedText('city', "", placeholder="eg.: Vancouver"), css_class='form-group col-md-6 mb-0'),
                Column('province', css_class='form-group col-md-4 mb-0'),
                Column(PrependedText('postal_code', "", placeholder="eg.: V1T 1TV"),
                       css_class='form-group col-md-2 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    def save(self, user):
        if self.is_valid():
            data = self.cleaned_data
            address_instance = Address(user=user, **data)
            address_instance.lat, address_instance.long = get_latitude_longitude(address_instance)
            address_instance.save()
            return True
        return False


"""
class CreateAddress(forms.Form):
    #  https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'street address (eg.: 1234 Name St)'}))
    unit = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'unit number (eg.: 123) - optional'}),
                           required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city name'}))
    province = forms.ChoiceField(choices=Province().ProvincesChoices.choices, initial=Province().ProvincesChoices.BC)
    postal_code = forms.CharField(label='Postal Code', widget=forms.TextInput(attrs={'placeholder': 'postal code'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('street', css_class='form-group col-md-8 mb-0'),
                Column('unit', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('province', css_class='form-group col-md-4 mb-0'),
                Column('postal_code', css_class='form-group col-md-2 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    def save(self, user):
        if self.is_valid():
            data = self.cleaned_data
            data["province"] = Province.objects.get(code=data["province"])
            address_instance = Address(user=user, **data)
            address_instance.lat, address_instance.long = get_latitude_longitude(address_instance)
            address_instance.save()
            return True
        return False
"""
