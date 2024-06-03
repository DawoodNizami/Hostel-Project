from .models import HostelAd
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import HostelAdForm
from django.db.models import Q
from .forms import CustomUserCreationForm


@login_required
def profile(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, "profile.html", {"form": form})


@login_required
def post_ad(request):
    if not request.user.is_owner:
        return redirect("index")
    if request.method == "POST":
        form = HostelAdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            return redirect("my_ads")
    else:
        form = HostelAdForm()
    return render(request, "post_ad.html", {"form": form})


# def post_ad(request):
#     if not request.user.is_authenticated or not request.user.is_owner:
#         return redirect("login")
#     # Handle ad posting here
#     return render(request, "post_ad.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def my_ads(request):
    if not request.user.is_owner:
        return redirect("index")
    ads = HostelAd.objects.filter(owner=request.user)
    return render(request, "my_ads.html", {"ads": ads})


@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(HostelAd, pk=ad_id, owner=request.user)
    if request.method == "POST":
        form = HostelAdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect("my_ads")
    else:
        form = HostelAdForm(instance=ad)
    return render(request, "edit_ad.html", {"form": form})


@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(HostelAd, pk=ad_id, owner=request.user)
    if request.method == "POST":
        ad.delete()
        return redirect("my_ads")
    return render(request, "delete_ad.html", {"ad": ad})


def index(request):
    query = request.GET.get("q")
    ads = HostelAd.objects.all()
    if query:
        ads = ads.filter(Q(city__icontains=query) | Q(area__icontains=query))
    return render(request, "index.html", {"ads": ads})


def detail(request, ad_id):
    ad = get_object_or_404(HostelAd, pk=ad_id)
    return render(request, "detail.html", {"ad": ad})
