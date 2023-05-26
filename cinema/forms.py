from urllib import request

from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    client_name = forms.CharField(label="Імʼя")
    client_email = forms.CharField(label="Пошта")
    client_phone = forms.CharField(label="Телефон:")
    place_num = forms.CharField(label="Номер місця")

    class Meta:
        model = Reservation
        fields = ['client_name', 'client_email', 'client_phone', 'place_num', 'session_id']
