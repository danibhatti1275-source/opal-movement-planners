from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vendor, EventPackage, ContactInfo, VendorCategory
from .forms import BookingForm

def home(request):
    context = {
        'packages': EventPackage.objects.filter(is_active=True)[:4],
    }
    return render(request, 'home.html', context)

def photographers(request):
    vendors = Vendor.objects.filter(category__name__in=['Photography', 'Photographer'], is_active=True)
    return render(request, 'photographers.html', {'vendors': vendors, 'title': 'Photography Partners'})

def decorators(request):
    vendors = Vendor.objects.filter(category__name__in=['Decor', 'Decore', 'Decorators'], is_active=True)
    return render(request, 'decorators.html', {'vendors': vendors, 'title': 'Decor Partners'})

def caterers(request):
    vendors = Vendor.objects.filter(category__name__in=['Catering', 'Caterer'], is_active=True)
    return render(request, 'caterers.html', {'vendors': vendors, 'title': 'Catering Partners'})

def packages(request):
    walima_packages = EventPackage.objects.filter(event_type='walima', is_active=True)
    other_packages = EventPackage.objects.filter(is_active=True).exclude(event_type='walima')
    return render(request, 'packages.html', {
        'walima_packages': walima_packages,
        'other_packages': other_packages
    })

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking request submitted successfully! We will contact you soon.')
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def contact(request):
    contacts = ContactInfo.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})