from django.contrib import admin

from .models import ShoppingCart, Card


# Register your models here.

class AdminCard(admin.ModelAdmin):
    list_display = ['UserID', 'CardID']

    class Meta:
        model = Card


class AdminShoppingCart(admin.ModelAdmin):
    list_display = ['UserID', 'ProductName', 'ProductPrice', 'Name']

    class Meta:
        model = ShoppingCart


admin.site.register(ShoppingCart, AdminShoppingCart)
admin.site.register(Card, AdminCard)
