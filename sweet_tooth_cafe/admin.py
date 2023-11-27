from django.contrib import admin

from sweet_tooth_cafe.models import Customer, Candy, Wishlist, Discount

admin.site.site_header = 'The Sweet Tooth Confectionery'


class CandyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'flavour', 'category_name', 'quantity', 'in_inventory', 'add_ons', 'cost', 'price',
                    'discount_id', 'rating', 'image', 'modified_at', 'created_at']
    search_fields = ['brand', 'flavour', 'category_name', 'cost', 'price']
    list_per_page = 20


admin.site.register(Candy, CandyAdmin)


# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_subscribed', 'profile_pic', 'modified_at', 'created_at']
    list_filter = ['is_subscribed']
    search_fields = ['first_name', 'last_name', 'email', 'created_at', 'modified_at']
    list_per_page = 20


admin.site.register(Customer, CustomersAdmin)


class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'amount','min_spend', 'max_discount', 'image', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'code', 'amount','min_spend', 'max_discount']
    list_per_page = 20


admin.site.register(Discount, DiscountsAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'modified_at']
    search_fields = ['created_at', 'modified_at']
    list_per_page = 25


admin.site.register(Wishlist, WishlistAdmin)
