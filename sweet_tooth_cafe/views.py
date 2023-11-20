from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from sweet_tooth_cafe.forms import LoginForm, SignupForm
from sweet_tooth_cafe.models import Customer


# Create your views here.

def home(request):
    return render(request, 'pages/landing_page.html')


def store(request):
    return render(request, 'pages/store.html')


def blog(request):
    return render(request, 'pages/blog.html')


def contact_us(request):
    return render(request, 'pages/contact.html')


@login_required
def cart(request):
    return render(request, 'pages/cart.html')


def all_candy(request):
    return render(request, 'pages/all_candy.html')


def about(request):
    return render(request, 'pages/about.html')


def deals(request):
    return render(request, 'pages/deals.html')


@login_required()
def checkout(request):
    return None


def categories(request):
    return render(request, 'pages/categories.html')


def login(request):
    @csrf_protect
    def customer_login(request):
        csrf_context = RequestContext(request)
        return render(request, 'pages/login.html', csrf_context)

    if request.method == 'POST':
        # Load the form with data from your request
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'You have signed up successfully!')
            return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'login_form': form})


def signup(request):
    @csrf_protect
    def customer_signup(request):
        csrf_context = RequestContext(request)
        return render(request, 'pages/signup.html', csrf_context)

    if request.method == 'POST':
        # Load the form with data from your request
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'pages/signup.html', {'signup_form': form})

@login_required()
def settings(request):
    return render(request, 'pages/settings.html')


@login_required()
def wishlist(request):
    return render(request, 'pages/wishlist.html')


@login_required()
def customer_home(request):
    return render(request, 'pages/customer_homepage.html')
