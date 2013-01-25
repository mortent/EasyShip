import datetime
from django.core import exceptions
from django.utils.translation import ugettext_lazy as _

def validate_zipcode(value):
    DIGITS = [str(x) for x in range(0,10)]
    for char in value:
        if char in DIGITS:
            continue
        raise exceptions.ValidationError(_("Zipcode can only contain digits."))

def validate_date_today_or_later(value):
    if value < datetime.date.today():
        raise exceptions.ValidationError(_('Date must be today or later'))
