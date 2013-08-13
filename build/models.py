from django.core.urlresolvers import reverse
from django.db import models


class NetworkAddress(models.Model):
    
    ip_address = models.CharField(
        max_length=25, unique=True,
    )
    subnet_mask = models.CharField(
        max_length=25,
    )
    
    def __str__(self):

        return ' '.join([
            self.ip_address,
            self.subnet_mask,
        ])
    
    def get_absolute_url(self):
        
        return reverse('networkaddress-view', kwargs={'pk': self.id})


class NetworkDevice(models.Model):
    
    networkaddress = models.ForeignKey(NetworkAddress)
    device_type = models.CharField(max_length=255,)
    
    class Meta:
        unique_together = ('networkaddress', 'device_type',)
        
