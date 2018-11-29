from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            # 'billing_profile', # It should NOT display to user
            # 'address_type', #This also come with logic
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code',

        ]
