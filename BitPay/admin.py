from django.contrib import admin

from .models import BitPayment


# Register your models here.

class AdminBitPay(admin.ModelAdmin):
    list_display = ['UserID', 'USD', 'Satoshi', 'PaidSatoshi', 'Status', 'ProductItem']

    class Meta:
        model = BitPayment


admin.site.register(BitPayment, AdminBitPay)
