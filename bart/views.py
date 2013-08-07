from django.shortcuts import render

def index_page(request):
	return render(request, 'bart/index.html', {})

def contact_page(request):
    return render(request, 'bart/contact.html', {})

def about_page(request):
    return render(request, 'bart/about.html', {})
