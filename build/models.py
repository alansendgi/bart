# -*- coding: utf-8 -*-
# Import the basic Django ORM models library
from django.db import models

# Import the reverse lookup function
from django.core.urlresolvers import reverse


class NetworkAddress(models.Model):
    
    ip_address = models.IPAddressField()
    subnet_mask = models.IPAddressField()
    description = models.CharField(max_length=255)
    
    def __unicode__(self):

        return ' '.join([self.ip_address, self.subnet_mask])
    
    def get_absolute_url(self):
        
        return reverse('networkaddress-view', kwargs={'pk': self.id})


class NetworkDevice(models.Model):
    
    networkaddress = models.ForeignKey(NetworkAddress)
    device_type = models.CharField(max_length=20,)
    fqdn = models.CharField(max_length=255,)
    community = models.CharField(max_length=255,)
    username = models.CharField(max_length=255,)
    password = models.CharField(max_length=255,)
    manufacturer = models.CharField(max_length=255,)
    model_no = models.CharField(max_length=255,)
    
    class Meta:
        unique_together = ('networkaddress', 'device_type',)
