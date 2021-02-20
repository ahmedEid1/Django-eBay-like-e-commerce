from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Category, Bid, Comment
from .forms import ListingForm, BidingForm


def index(request):
    listings = Listing.objects.filter(active=True)

    return render(request, "auctions/index.html", {'listings': listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            listing = Listing(owner=request.user, title=data['title'], description=data['description'],
                              starting_bid=data['starting_bid'])
            if data['image'] is not None:
                listing.image = data['image']
            if data['category'] is not None:
                listing.category = data['category']
            listing.save()
            return HttpResponseRedirect(reverse('listing_view', args=[listing.id]))
        else:
            return render(request, 'auctions/listing/create.html', {'form': form})

    return render(request, 'auctions/listing/create.html', {'form': ListingForm()})


def show_listing(request, pk):
    listing = Listing.objects.get(pk=pk)
    if listing.bids.count() == 0:
        min_bid = listing.starting_bid + 1
    else:
        min_bid = listing.bids.first().price + 1

    if request.method == 'POST':
        form = BidingForm(request.POST, min_bid=min_bid)
        if form.is_valid():
            bid = form.cleaned_data['bidding']
            new_bid = Bid(owner=request.user, listing=listing, price=bid)
            new_bid.save()
            return render(request, 'auctions/listing/view.html', {
                'listing': listing,
                'biding_form': form
            })
        else:
            return render(request, 'auctions/listing/view.html', {
                'listing': listing,
                'biding_form': form
            })

    return render(request, 'auctions/listing/view.html', {
        'listing': listing,
        'biding_form': BidingForm(min_bid=min_bid)
    })


def close_listing(request, pk):
    if request.method == "POST":
        listing = Listing.objects.get(pk=pk)
        listing.active = False
        if listing.bids.count() != 0:
            listing.winner = listing.bids.first().owner
        listing.save()

    return HttpResponseRedirect(reverse('listing_view', args=[pk]))


def comment(request, pk):
    if request.method == 'POST':
        author = request.user
        listing = Listing.objects.get(pk=pk)
        new_comment = Comment(author=author, listing=listing, content=request.POST['content'])
        new_comment.save()
        return HttpResponseRedirect(reverse('listing_view', args=[pk]))

    return HttpResponseRedirect(reverse('listing_view', args=[pk]))


def watch_list(request, pk):
    if request.method == 'POST':
        Listing.objects.get(pk=pk).watchers.add(request.user)

    return HttpResponseRedirect(reverse('listing_view', args=[pk]))


def stop_watch(request, pk):
    if request.method == 'POST':
        Listing.objects.get(pk=pk).watchers.remove(request.user)

    return HttpResponseRedirect(reverse('listing_view', args=[pk]))


def show_watch_list(request):
    return render(request, "auctions/listing/watchlist.html", {'listings': request.user.watch_list.all()})


def show_categories(request):
    return render(request, "auctions/categories.html", {'categories': Category.objects.all()})


def show_category_listing(request, pk):
    return render(request, "auctions/category.html", {'category': Category.objects.get(pk=pk)})
