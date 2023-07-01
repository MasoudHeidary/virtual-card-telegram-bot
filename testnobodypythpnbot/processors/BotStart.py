from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from ..bot import state_manager, TelegramBot
from ..models import TelegramState

from .component import HomeKeyboard
from .BotSettings import BotName


@processor(
    state_manager,
    from_states=state_types.Reset,
    success='/Home',
    fail=state_types.Keep,
    update_types=update_types.Message,
    message_types=message_types.Text
)
def start(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    # user_name = update.get_user().get_username()

    bot.sendMessage(
        chat_id,
        f"Welcome to {BotName}",
        reply_markup=HomeKeyboard
    )
