from django.db import models

class IPAddress(models.Model):
    ipaddress = models.IPAddressField(primary_key=True)
    fqdn = models.CharField(max_length=255)
    community = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return u"%s" % (self.ipaddress)


class NetworkDevice(models.Model):
    ipaddress = models.ForeignKey(IPAddress)
    manufacturer = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ios = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.fqdn


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class HardwareComponent(models.Model):
    manufacturer = models.CharField(max_length=50)
    #types include video card, network card...
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    vendor_part_number = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.manufacturer


class Server(models.Model):
    ipaddress = models.ForeignKey(IPAddress)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    os = models.ForeignKey(OperatingSystem)
    services = models.ManyToManyField(Service)
    hardware_component = models.ManyToManyField(HardwareComponent)

    def __unicode__(self):
        return self.name


