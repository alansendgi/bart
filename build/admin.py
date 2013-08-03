from django.contrib import admin
from build.models import NetworkAddress
# changed polls.models to build.models, Poll to NetworkAddress
from build.models import NetworkDevice
# changed polls.models to build.models, Choice to NetworkDevice


class NetworkAddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Network Address',     {'fields': ['address']}),
        (None,                  {'fields': ['network_size']}),
        ('Date information',    {'fields': ['add_date']}),
    ]
    list_display = ('address', 'network_size', 'add_date')


class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_model', 'networkaddress', 'subnet_addr')
    

admin.site.register(NetworkAddress, NetworkAddressAdmin)
admin.site.register(NetworkDevice, NetworkDeviceAdmin)
