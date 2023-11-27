from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from sweet_tooth_cafe import models
from sweet_tooth_cafe.forms import LoginForm, SignupForm
from sweet_tooth_cafe.models import Customer, Candy


# Create your views here.

def home(request):
    today = datetime.today()
    month = today.month
    latest_candy = Candy.objects.filter(created_at__month=month).order_by('flavour')
    return render(request, 'pages/landing_page.html', {'latest_candy': latest_candy})


def blog(request):
    return render(request, 'pages/blog.html')


def contact_us(request):
    return render(request, 'pages/contact.html')


@login_required
def cart(request):
    return render(request, 'pages/cart.html')


def all_candy(request):
    candy_data = Candy.objects.all().order_by('flavour')
    brands = models.Candy.objects.order_by('brand').values('brand').distinct()
    categories = models.Candy.objects.order_by('category_name').values('category_name').distinct()
    flavours = models.Candy.objects.order_by('flavour').values('flavour').distinct()
    paginator = Paginator(candy_data, 20)
    page_number = request.GET.get('page')
    candy_data = paginator.get_page(page_number)
    return render(request, 'pages/all_candy.html', {'candies': candy_data, 'brands': brands,
                                                    'categories': categories, 'flavours': flavours})


def show_brands(request, brand):
    candy = models.Candy.objects.filter(brand=brand)
    brands = models.Candy.objects.values('brand')
    brand_name = {'brand_name': brand}
    return render(request, 'pages/brand_category.html', {'candy': candy, 'brands': brands, 'brand_name': brand_name})


def about(request):
    return render(request, 'pages/about.html')

@login_required()
def checkout(request):
    return None


def deals(request):
    discounts = models.Discount.objects.filter(is_active=True).order_by('name')
    return render(request, 'pages/deals.html', {'discounts': discounts})


def categories(request):
    categories = models.Candy.objects.order_by('category_name').values('category_name').distinct()
    return render(request, 'pages/categories.html', {'category': categories})


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


def store(request):
    candies = Candy.objects.all()
    brands = models.Candy.objects.order_by('brand').values('brand').distinct()
    return render(request, 'pages/store.html', {'candies': candies, 'brands': brands})


@login_required()
def wishlist(request):
    return render(request, 'pages/wishlist.html')


@login_required()
def customer_home(request):
    return render(request, 'pages/customer_homepage.html')


def products_details(request, candy_id):
    candy = Candy.objects.get(pk=candy_id)
    brands = models.Candy.objects.values_list('brand').distinct()
    return render(request, 'pages/product_details.html', {'candy': candy, 'brand': brands})


def search_candy(request):
    search_key = request.GET['search']
    candy_data = Candy.objects.filter(
        Q(flavour__icontains=search_key) |
        Q(brand__icontains=search_key) |
        Q(category_name__icontains=search_key) |
        Q(price=search_key) |
        Q(add_ons__icontains=search_key)
    )
    if search_key.isnumeric():
        price = int(search_key)
        candy_data = Candy.objects.filter(price=price)

    paginator = Paginator(candy_data,15)
    page_number = request.GET.get('page')
    candy_data = paginator.get_page((page_number))
    return render(request, 'pages/all_candy.html', {'candies': candy_data})


def show_categories(request, category):
    candy = models.Candy.objects.filter(category_name__icontains=category)
    cat_name = {'cat_name': category}
    category = models.Candy.objects.values('category_name')
    return render(request, 'pages/product_categories.html', {'candy': candy, 'category': category, 'cat_name': cat_name})


def show_flavours(request, flavour):
    candy = models.Candy.objects.filter(flavour__icontains=flavour)
    flavour_name = {'flavour_name': flavour}
    flavour = models.Candy.objects.values('flavour')
    return render(request, 'pages/product_categories.html',
                  {'candy': candy, 'flavour': flavour, 'flavour_name': flavour_name})


def product_deals(request, id):
    discount = models.Discount.objects.get(pk=id)
    discount_candy = models.Candy.objects.filter(discount_id=id).order_by('flavour')
    return render(request, 'pages/product_deals.html', {'discount_candy': discount_candy, 'discount': discount})