from django.shortcuts import render

from audit.models import IPAddress

def audit_main(request):
    ip_address_list = IPAddress.objects.all().order_by('-ipaddress')[:5]
    context = {'ip_address_list': ip_address_list}
    return render(request, 'audit/index.html', context)
