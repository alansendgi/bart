from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from build.models import (
    NetworkDevice,
    NetworkAddress,
)


class NetworkDeviceForm(forms.ModelForm):

    class Meta:
        model = NetworkDevice

    def __init__(self, *args, **kwargs):

        return super(NetworkDeviceForm, self).__init__(*args, **kwargs)


# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)
NetworkDeviceAddressFormSet = inlineformset_factory(
    NetworkDevice,
    NetworkAddress,
)
