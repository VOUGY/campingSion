from django.forms import ModelForm
from .models import Booking
from geo_web.models import Location
from django import forms


class BookForm(ModelForm):

    location_id = forms.IntegerField()

    class Meta:
        model = Booking
        fields = ['lastname', 'firstname', 'email', 'tel_number', 'date_start', 'date_end', 'location_id']

    def save(self, location_id=None):
        booking = super(BookForm, self).save(commit=False)
        booking.save()

        location = Location.objects.get(id_0=self.cleaned_data['location_id'])
        location.bookings.add(booking)
        location.save()

        return booking
