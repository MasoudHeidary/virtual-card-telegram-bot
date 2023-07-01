from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from ..bot import state_manager, TelegramBot
from ..models import TelegramState

from .BotDialogs import go_home, go_buy_card, go_get_name
from .component import BuyCardOptionKeyboard, BackHomeKeyboard


@processor(
    state_manager,
    from_states='/BuyCardOption',
    update_types=update_types.Message,
    message_types=message_types.Text
)
def buy_card_option(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    message_text = update.get_message().get_text()

    if message_text == 'USA Virtual Debit Card':
        state.set_name('/BuyCard')
        go_buy_card(chat_id, bot)

    elif message_text == 'PayPal Verification Card(4.99$)':
        state.set_memory({'ProductName': 'PayPal verification card', 'ProductValue': 1, 'ProductPrice': 4.99})
        go_get_name(chat_id, bot)
        state.set_name('/BuyCard_Name')
        # bot.sendMessage(chat_id, 'We try to add this feature, as soon as possible')

    elif message_text == 'Home':
        state.set_name('/Home')
        go_home(chat_id, bot)

    else:
        bot.sendMessage(
            chat_id,
            f"I can't recognize {message_text} command\n"
            f"Please use reply keyboard",
            reply_markup=BuyCardOptionKeyboard
        )


@processor(
    state_manager,
    from_states='/BuyCard',
    update_types=update_types.CallbackQuery,
    message_types=message_types.Text
)
def buy_card(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    value = update.get_callback_query().get_data()

    value = value.split(',')
    product_name = value[0]
    product_value = int(value[1])
    product_price = float(value[2])
    state.set_memory({'ProductName': product_name, 'ProductValue': product_value, 'ProductPrice': product_price})

    go_get_name(chat_id, bot)
    state.set_name('/BuyCard_Name')


@processor(
    state_manager,
    from_states='/BuyCard',
    update_types=update_types.Message,
    message_types=message_types.Text
)
def buy_card_text(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    message_text = update.get_message().get_text()

    if message_text == 'Home':
        state.set_name('/Home')
        go_home(chat_id, bot)
    else:
        bot.sendMessage(
            chat_id,
            f"I can't recognize {message_text} command\n"
            f"Please use reply keyboard",
            reply_markup=BackHomeKeyboard
        )
