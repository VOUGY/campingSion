from django.forms import ModelForm
from .models import Booking


class BookForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['lastname', 'firstname', 'email', 'tel_number', 'date_start', 'date_end']