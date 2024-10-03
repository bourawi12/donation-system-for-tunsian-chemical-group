from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def main_view(request):
    return render(request,'views/main.html', {"name":"autoMax"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listings': listings,
        'lisitng_filter':listing_filter
    }
    return render(request, "views/home.html", context)  # Pass context here

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST,request.FILES)
            location_form = LocationForm(request.POST,)
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location= location_form.save()
                listing.seller = request.user.profile
                lislocation = listing_location
                listing.save()
                messagesinfo(request,f'{listing.model} Listing Posted successfully')
                return redirect('home')
        except Exception as e :
            print(e)
            messages.error(request,'error occured while posting')
    elif request.method =='GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request,'views/list.html', {'listing_form':listing_form,'location_form':location_form})

@login_required
def listing_view(request, id):
    try :
        listing = Listing.objects.get(id=id)
        if listing is None : 
            raise Exception
        return render(request, 'views/lisitng.html', {'listing' : listing, })
    except Exception as e :
        messages.error(request,f'invalid uid {id} was provided for listings')
        return redirect('home')
        
    
