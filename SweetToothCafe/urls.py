"""
URL configuration for SweetToothCafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from SweetToothCafe import settings
from sweet_tooth_cafe import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-candy/', views.all_candy, name='all_candy'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('brand/<str:brand>', views.show_brands, name='brand_categories'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('deals/', views.deals, name='deals'),
    path('deals/<int:id>', views.product_deals, name='product_deals'),
    path('checkout/', views.checkout, name='checkout'),
    path('customer-home/<int:customer_id>', views.customer_home, name='customer_home'),
    path('categories/', views.categories, name='categories'),
    path('login/', views.login, name='login'),
    path('product_category/<str:category>', views.show_categories, name='product_categories'),
    path('product-details/<int:candy_id>', views.products_details, name='product_details'),
    path('product-flavour/<str:flavour>', views.show_flavours, name='product_flavours'),
    path('search-candy', views.products_details, name='search_candy'),
    path('settings/', views.settings, name='settings'),
    path('signup/', views.signup, name='signup'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
