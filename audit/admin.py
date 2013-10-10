from django.contrib import admin
from audit.models import *

admin.site.register(OperatingSystem)
admin.site.register(Service)
admin.site.register(HardwareComponent)
admin.site.register(Server)
admin.site.register(IPAddress)
admin.site.register(NetworkDevice)

