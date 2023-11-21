from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from sweet_tooth_cafe.forms import LoginForm, SignupForm
from sweet_tooth_cafe.models import Customer, Candy


# Create your views here.

def home(request):
    return render(request, 'pages/landing_page.html')




def blog(request):
    return render(request, 'pages/blog.html')


def contact_us(request):
    return render(request, 'pages/contact.html')


@login_required
def cart(request):
    return render(request, 'pages/cart.html')


def all_candy(request):
    candy_data = Candy.objects.all().order_by('flavour')
    paginator = Paginator(candy_data, 20)
    page_number = request.GET.get('page')
    candy_data = paginator.get_page(page_number)
    return render(request, 'pages/all_candy.html', {'candies': candy_data})


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
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'pages/login.html', {'login_form': login_form})


    elif request.method == 'POST':
        # Load the form with data from your request
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Sign in was successful!')
                return redirect('home')

        messages.error(request, 'Invalid username or password!')
        return render(request, 'pages/login.html', {'login_form': login_form})


def customer_home(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)

    return render(request, 'pages/customer_homepage.html', {'customer': customer})


def store(request):
    candy_data = Candy.objects.all()
    return render(request, 'pages/store.html', {'candies': candy_data})


def signup(request):
    @csrf_protect
    def customer_signup(request):
        csrf_context = RequestContext(request)
        return render(request, 'pages/signup.html', csrf_context)

    if request.method == 'POST':
        # Load the form with data from your request
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'pages/customer_homepage.html')

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
