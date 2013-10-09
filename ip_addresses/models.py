from django.db import models
from django.forms import ModelForm
import socket


class NetworkAddress(models.Model):
    address = models.IPAddressField()
    network_size = models.PositiveIntegerField()
    description = models.CharField(max_length=400)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return "%s/%d" % (self.address, self.network_size)

    @models.permalink
    def get_absolute_url(self):
        return ('networkaddress-display', (), {'address': '%s/%s' % (self.address, self.network_size)})

    def get_hostname(self):
        try:
            fqdn = socket.gethostbyaddr(str(self.address))[0]
        except:
            fqdn = ''
        return fqdn

    def get_formated_address(self):
        return str(self.address).replace('.', '_')

    def get_netmask(self):
        bit_netmask = 0;
        bit_netmask = pow(2, self.network_size) - 1
        bit_netmask = bit_netmask << (32 - self.network_size)
        nmask_array = []
        for c in range(4):
            dec = bit_netmask & 255
            bit_netmask = bit_netmask >> 8
            nmask_array.insert(0, str(dec))
        return ".".join(nmask_array)


class NetworkAddressAddForm(ModelForm):
    class Meta:
        model = NetworkAddress
        exclude = ('parent', )


class NetworkAddressModifyForm(ModelForm):
    class Meta:
        model = NetworkAddress
        fields = ('description',)


class DomainName(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=400)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.comment[:20])


# NETWORKDEVICE model classes

class NetworkDevice(models.Model):
    address = models.ForeignKey(NetworkAddress)
    community = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    fqdn = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    ios = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.address, self.fqdn, self.community, self.model)

