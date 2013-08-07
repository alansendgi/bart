from django.contrib import admin
from build.models import NetworkDevice


class NetworkDeviceAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(NetworkDevice, NetworkDeviceAdmin)
