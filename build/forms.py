# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory

from build.models import NetworkAddress
from build.models import NetworkDevice


# inlineformset_factory creates a Class from a parent model (NetworkAddress)
# to a child model (NetworkDevice)
NetworkDeviceFormSet = inlineformset_factory(
    NetworkAddress,
    NetworkDevice,
    can_delete=False,
    extra=1,
    max_num=1
)
