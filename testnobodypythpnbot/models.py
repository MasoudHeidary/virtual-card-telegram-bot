from django.db import models
from django.db.models import CASCADE

from django_tgbot.models import AbstractTelegramUser, AbstractTelegramChat, AbstractTelegramState


class TelegramUserManager(models.Manager):
    def search_user_id(self, user_id):
        qu = self.get_queryset().filter(telegram_id=user_id)
        if qu.exists():
            return qu.first()
        else:
            return None

    def get_by_user_id(self,user_id):
        qu = self.get_queryset().filter(telegram_id=user_id)
        if not qu.exists():
            return False
        else:
            return qu.first()



class TelegramUser(AbstractTelegramUser):
    object = TelegramUserManager()


class TelegramChat(AbstractTelegramChat):
    pass


class TelegramState(AbstractTelegramState):
    telegram_user = models.ForeignKey(TelegramUser, related_name='telegram_states', on_delete=CASCADE, blank=True,
                                      null=True)
    telegram_chat = models.ForeignKey(TelegramChat, related_name='telegram_states', on_delete=CASCADE, blank=True,
                                      null=True)

    class Meta:
        unique_together = ('telegram_user', 'telegram_chat')
