from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from ..bot import state_manager, TelegramBot
from ..models import TelegramState

from .BotDialogs import go_home, go_shopping_cart, go_pay_off

from CardManager.models import ShoppingCart


@processor(
    state_manager,
    from_states='/ShoppingCart',
    update_types=update_types.Message,
    message_types=message_types.Text
)
def shopping_cart(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    message_text = update.get_message().get_text()
    user_id = update.get_user().get_id()

    if message_text == 'Home':
        state.set_name('/Home')
        go_home(chat_id, bot)
    elif 'Your Invoice' in message_text:
        go_pay_off(chat_id, user_id, bot)
        state.set_name('/Home')
        go_home(chat_id, bot)


@processor(
    state_manager,
    from_states='/ShoppingCart',
    update_types=update_types.CallbackQuery,
    message_types=message_types.Text
)
def shopping_cart_remove(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    value = update.get_callback_query().get_data()
    user_id = update.get_user().get_id()

    if ShoppingCart.object.remove_by_item_id(user_id=user_id, item_id=value):
        if not go_shopping_cart(chat_id, user_id, bot):
            go_home(chat_id, bot)
            state.set_name('/Home')
        # else:
            # go_shopping_cart(chat_id, user_id, bot)
    else:
        bot.sendMessage(chat_id, f"Your item {value}, can't be found")
