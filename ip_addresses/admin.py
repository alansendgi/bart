from ip_addresses.models import *
from django.contrib import admin

class NetworkAddressAdmin(admin.ModelAdmin):
    pass

class DomainNameAdmin(admin.ModelAdmin):
    pass

class NetworkDeviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(NetworkAddress, NetworkAddressAdmin)
admin.site.register(DomainName, DomainNameAdmin)
admin.site.register(NetworkDevice, NetworkDeviceAdmin)
