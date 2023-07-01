from django.contrib import admin
from .models import *


class AdminTelegramChatView(admin.ModelAdmin):
    list_display = ['telegram_id', 'type', 'username']

    class Meta:
        model = TelegramChat


class AdminTelegramUserView(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'first_name', 'last_name', 'is_bot']

    class Meta:
        model = TelegramUser


class AdminTelegramStateView(admin.ModelAdmin):
    list_display = ['name', 'telegram_user', 'telegram_chat', 'memory']

    class Meta:
        model = TelegramState


admin.site.register(TelegramChat, AdminTelegramChatView)
admin.site.register(TelegramUser, AdminTelegramUserView)
admin.site.register(TelegramState, AdminTelegramStateView)
