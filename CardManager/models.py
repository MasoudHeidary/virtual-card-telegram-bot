from django.db import models

from testnobodypythpnbot.models import TelegramUser


# Create your models here.
class CardManager(models.Manager):
    def get_by_user_id(self, user_id):
        qu = self.get_queryset().filter(UserID__telegram_id__exact=user_id)
        if qu.exists():
            return qu
        else:
            return False


class Card(models.Model):
    UserID = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    CardID = models.CharField(max_length=100, default='None')
    # City = models.CharField(max_length=30, default='None')
    # State = models.CharField(max_length=30, default='None')
    # Address = models.CharField(max_length=100, default='None')
    # ZipCode = models.CharField(max_length=10, default='None')
    # CardPan = models.CharField(max_length=20, default='None')
    # CVV = models.CharField(max_length=10, default='None')
    # Expiration = models.CharField(max_length=30, default='None')
    # Name = models.CharField(max_length=50, default='None')
    # Amount = models.CharField(max_length=20, default='None')

    object = CardManager()


class ShoppingCartManager(models.Manager):
    def get_by_user_id(self, user_id):
        qu = self.get_queryset().filter(UserID__telegram_id__exact=user_id)
        if qu.exists():
            return qu
        else:
            return False

    def get_by_user_id_and_item_id(self, user_id, item_id):
        qu = self.get_queryset().filter(UserID__telegram_id__exact=user_id, ItemID__exact=item_id)
        if not qu.exists():
            return False
        else:
            return qu.first()

    def get_next_item_id(self, user_id):
        qu = self.get_queryset().filter(UserID__telegram_id__exact=user_id)
        if not qu.exists():
            return 0
        else:
            return qu.latest('ItemID').ItemID + 1

    def remove_by_item_id(self, user_id, item_id):
        qu = self.get_queryset().filter(UserID__telegram_id=user_id, ItemID__exact=item_id)
        if not qu.exists():
            return False
        else:
            qu.filter().delete()
            return True


class ShoppingCart(models.Model):
    UserID = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    ItemID = models.IntegerField()
    ProductName = models.CharField(max_length=50)
    ProductValue = models.IntegerField()
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Name = models.CharField(max_length=100)
    # Street = models.CharField(max_length=150)
    # City = models.CharField(max_length=100)
    # State = models.CharField(max_length=2)
    # ZipCode = models.CharField(max_length=5)

    object = ShoppingCartManager()
