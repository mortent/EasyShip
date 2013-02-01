from django import forms
import validators
from root.models import ServiceLevel
from django.utils.translation import ugettext_lazy as _


class ZipcodeField(forms.CharField):
    default_error_messages = {
        'invalid': _('Enter a valid zip code.'),
        }
    default_validators =  [validators.validate_zipcode]


class TodayOrLaterDateField(forms.DateField):
    default_error_messages = {
        'invalid': _('Enter a valid date.'),
    }
    default_validators = [validators.validate_date_today_or_later]

class WeightField(forms.CharField):
    default_error_messages = {
        'invalid': _('Enter a valid weight'),
        }
    default_validators = [validators.validate_weight]

class SearchForm(forms.Form):
    """
    SearchForm to collect the search parameters for our search page. It uses custom Fields with custom validators.
    """
    zip_code = ZipcodeField(max_length=5, min_length=5)
    weight = WeightField(max_length=6, min_length=1)
    service_level = forms.ModelMultipleChoiceField(queryset=ServiceLevel.objects.all())
    shipping_date = TodayOrLaterDateField()

