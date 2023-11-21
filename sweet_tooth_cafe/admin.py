from django.contrib import admin

from sweet_tooth_cafe.models import Customer, Candy, Wishlist

admin.site.site_header = 'The Sweet Tooth Cafe'


# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_subscribed', 'profile_pic', 'modified_at', 'created_at']
    list_filter = ['is_subscribed']
    search_fields = ['first_name', 'last_name', 'email', 'created_at', 'modified_at']
    list_per_page = 20


admin.site.register(Customer, CustomersAdmin)


class CandyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'category', 'flavour', 'quantity', 'in_inventory', 'cost', 'price',
                    'rating', 'image', 'modified_at', 'created_at']
    search_fields = ['brand', 'cost', 'price']
    list_per_page = 25


admin.site.register(Candy, CandyAdmin)



class WishlistAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'modified_at']
    search_fields = ['created_at', 'modified_at']
    list_per_page = 25


admin.site.register(Wishlist, WishlistAdmin)
