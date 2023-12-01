from django.contrib import admin

from sweet_tooth_cafe.models import Customer, Candy, Wishlist, Discount, Order

admin.site.site_header = 'The Sweet Tooth Cafe'

# Register your models here.
@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'flavour', 'category_name', 'quantity', 'in_inventory', 'add_ons', 'price',
                    'discount_id', 'rating', 'image', 'modified_at', 'created_at']
    search_fields = ['brand', 'flavour', 'category_name', 'price']
    list_per_page = 15


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'gender', 'password', 'is_subscribed', 'profile_pic',
                    'modified_at', 'created_at']
    list_filter = ['is_subscribed', 'gender']
    search_fields = ['first_name', 'last_name', 'email', 'created_at', 'modified_at']
    list_per_page = 15


@admin.register(Discount)
class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'amount','min_spend', 'max_discount', 'image', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'code', 'amount','min_spend', 'max_discount']
    list_per_page = 15


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total', 'to_deliver', 'created_at', 'modified_at']
    list_filter = ['to_deliver']
    search_fields = ['id', 'customer', 'total', 'to_deliver']
    list_per_page = 15


