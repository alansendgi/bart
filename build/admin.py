# -*- coding: utf-8 -*-
from django.contrib import admin
from build.models import *

class NetworkAddressAdmin(admin.ModelAdmin):
    pass

class DomainNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(NetworkAddress, NetworkAddressAdmin)
admin.site.register(DomainName, DomainNameAdmin)
