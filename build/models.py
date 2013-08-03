from django.db import models

class NetworkAddress(models.Model):
    # changed Poll to NetworkAddress
    address = models.IPAddressField()
    # changed question to address
    network_size = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    add_date = models.DateTimeField('date added')
    # changed pub_date to add_date
    
    def was_added_recently(self):
        # changed was_published_recently to was_added_recently
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __unicode__(self):
        return self.address

class NetworkDevice(models.Model):
    # changed Choice to NetworkDevice
    device_model = models.CharField(max_length=100)
    # changed choice_text to device_model
    networkaddress = models.ForeignKey(NetworkAddress)
    # changed poll to networkaddress, Poll to NetworkAddress
    subnet_addr = models.IPAddressField(default='255.255.255.255')
    # changed votes to subnet_addr
    
    def __unicode__(self):
        return self.device_model
