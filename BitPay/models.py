from django.db import models

from testnobodypythpnbot.models import TelegramUser


# Create your models here.
class BitPaymentManager(models.Manager):
    def get_by_user_id(self,user_id):
        qu = self.get_queryset().filter(UserID__telegram_id=user_id)
        if not qu.exists():
            return False
        else:
            return qu.first()

    def get_by_address(self,address):
        qu = self.get_queryset().filter(Address__exact=address)
        if not qu.exists():
            return False
        else:
            return qu.first()


class BitPayment(models.Model):
    UserID = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    USD = models.DecimalField(max_digits=10, decimal_places=2)
    Satoshi = models.IntegerField()
    PaidSatoshi = models.IntegerField()
    Status = models.IntegerField()
    Time = models.IntegerField()
    TXID = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=250)
    ProductItem = models.CharField(max_length=100)

    object = BitPaymentManager()
