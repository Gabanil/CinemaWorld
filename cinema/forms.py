from urllib import request

from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    client_name = forms.CharField(label="Name")
    client_email = forms.CharField(label="Email")
    client_phone = forms.CharField(label="Phone")
    place_num = forms.IntegerField(label="Place Number")

    class Meta:
        model = Reservation
        fields = ['client_name', 'client_email', 'client_phone', 'place_num', 'session_id']
