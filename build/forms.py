from django import forms
from django.forms.models import inlineformset_factory

from build.models import (
    NetworkAddress,
    NetworkDevice,
)


# inlineformset_factory creates a Class from a parent model (NetworkAddress)
# to a child model (NetworkDevice)
NetworkDeviceFormSet = inlineformset_factory(
    NetworkAddress,
    NetworkDevice,
)
