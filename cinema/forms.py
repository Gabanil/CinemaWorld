from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('client_name', 'place_num', 'paid', 'date_resevation', 'session_id')

    client_name = forms.CharField(label="Name")
    place_num = forms.IntegerField(label="Place")
    paid = forms.BooleanField(label="Paid")
    date_resevation = forms.DateTimeField(label="Date")
    session_id = forms.IntegerField(label="Session")