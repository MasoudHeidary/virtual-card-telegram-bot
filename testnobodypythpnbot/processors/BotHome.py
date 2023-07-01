from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.exceptions import ProcessFailure
from ..bot import state_manager, TelegramBot
from ..models import TelegramState

from .component import HomeKeyboard
from .BotDialogs import go_buy_card_option, go_shopping_cart, go_home, go_my_card, join_channel
from .BotSettings import AdminContact, ChannelName


@processor(
    state_manager,
    from_states='/Home',
    fail=state_types.Keep,
    update_types=update_types.Message,
    message_types=message_types.Text
)
def home(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    message_text = update.get_message().get_text()
    user_id = update.get_user().get_id()

    if not join_channel(chat_id, user_id, bot):
        raise ProcessFailure

    if message_text == 'Order Virtual Card':
        state.set_name('/BuyCardOption')
        go_buy_card_option(chat_id, bot)

    elif message_text == 'Shopping Cart':
        state.set_name('/ShoppingCart')
        if not go_shopping_cart(chat_id, user_id, bot):
            go_home(chat_id, bot)
            state.set_name('/Home')

    elif message_text == 'My Cards':
        go_my_card(chat_id, user_id, bot)

    elif message_text == 'Contact Admin':
        bot.sendMessage(chat_id, AdminContact, reply_markup=HomeKeyboard)

    elif message_text == 'FAQs':
        bot.sendMessage(chat_id, ChannelName, reply_markup=HomeKeyboard)

    else:
        # handle unsupported message,
        bot.sendMessage(
            chat_id,
            "I can't recognize this command\nPlease use reply keyboard👇",
            reply_markup=HomeKeyboard
        )
