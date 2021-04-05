from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm
from django import forms

from circularis.books.models import Book
from circularis.books.services import clean_isbn, validate_isbn


class CreateBook(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_1', 'category', 'address', 'status', 'user']
        labels = {
            'author_1': 'Author',
        }

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].disabled = False


class SearchIsbnForm(forms.Form):
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Leave it blank or type the ISBN. It has 10 or 13 digits'}), required=False)

    def clean_isbn(self):
        data = self.cleaned_data['isbn']
        data = clean_isbn(data)

        if not validate_isbn(data):
            raise ValidationError(_('Invalid ISBN'))

        return data
