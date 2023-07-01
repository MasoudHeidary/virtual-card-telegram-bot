from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types
from django_tgbot.types.update import Update
from ..bot import state_manager, TelegramBot
from ..models import TelegramState

from .BotDialogs import go_home

# from .component import StateKeyboard
from CardManager.CardManagerRequest import add_in_shopping_cart


@processor(
    state_manager,
    from_states="/BuyCard_Name",
    update_types=update_types.Message,
    message_types=message_types.Text
)
def get_name(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    message_text = update.get_message().get_text()
    user_id = update.get_user().get_id()

    if message_text == 'Home':
        state.set_name('/Home')
        go_home(chat_id, bot)
    elif not message_text.isascii():
        bot.sendMessage(chat_id, 'EN')
    else:
        state.update_memory({'Name': message_text})
        data = state.get_memory()
        product_name = data.get('ProductName')
        product_value = data.get('ProductValue')
        product_price = data.get('ProductPrice')
        name = data.get('Name')

        add_in_shopping_cart(
            user_id=user_id,
            product_name=product_name,
            product_value=product_value,
            product_price=product_price,
            name=name,
        )
        state.reset_memory()

        bot.sendMessage(
            chat_id,
            'Added in shopping cart and waiting on your deposit',
        )

        state.set_name('/Home')
        go_home(chat_id, bot)

# @processor(
#     state_manager,
#     from_states="/BuyCard_Street",
#     update_types=update_types.Message,
#     message_types=message_types.Text
# )
# def get_street(bot: TelegramBot, update: Update, state: TelegramState):
#     chat_id = update.get_chat().get_id()
#     message_text = update.get_message().get_text()
#
#     if message_text == '/Home':
#         state.set_name('/Home')
#         go_home(chat_id, bot)
#     elif not message_text.isascii():
#         bot.sendMessage(chat_id, 'EN')
#     else:
#         state.update_memory({'Street': message_text})
#         go_get_city(chat_id, bot)
#         state.set_name('/BuyCard_City')


# @processor(
#     state_manager,
#     from_states="/BuyCard_City",
#     update_types=update_types.Message,
#     message_types=message_types.Text
# )
# def get_city(bot: TelegramBot, update: Update, state: TelegramState):
#     chat_id = update.get_chat().get_id()
#     message_text = update.get_message().get_text()
#
#     if message_text == '/Home':
#         state.set_name('/Home')
#         go_home(chat_id, bot)
#     elif not message_text.isascii():
#         bot.sendMessage(chat_id, 'EN')
#     else:
#         state.update_memory({'City': message_text})
#         go_get_state(chat_id, bot, state)
#         state.set_name('/BuyCard_State')


# @processor(
#     state_manager,
#     from_states="/BuyCard_State",
#     update_types=update_types.Message,
#     message_types=message_types.Text
# )
# def get_state(bot: TelegramBot, update: Update, state: TelegramState):
#     chat_id = update.get_chat().get_id()
#     message_text = update.get_message().get_text()
#
#     if message_text == '/Home':
#         state.set_name('/Home')
#         go_home(chat_id, bot)


# @processor(
#     state_manager,
#     from_states='/BuyCard_State',
#     update_types=update_types.CallbackQuery,
#     message_types=message_types.Text
# )
# def get_state_callback(bot: TelegramBot, update: Update, state: TelegramState):
#     chat_id = update.get_chat().get_id()
#     value = update.get_callback_query().get_data()
#     inline_id = update.get_callback_query().get_message().get_message_id()
#     page_number = state.get_memory().get('state_page')
#
#     if value == '/NextPage':
#         bot.editMessageReplyMarkup(chat_id, message_id=inline_id, reply_markup=StateKeyboard[page_number + 1])
#         state.update_memory({'state_page': page_number + 1})
#     elif value == '/PrevPage':
#         bot.editMessageReplyMarkup(chat_id, message_id=inline_id, reply_markup=StateKeyboard[page_number - 1])
#         state.update_memory({'state_page': page_number - 1})
#     else:
#         state.update_memory({'State': value})
#         go_get_zip_code(chat_id, bot)
#         state.set_name('/BuyCard_ZipCode')


# @processor(
#     state_manager,
#     from_states="/BuyCard_ZipCode",
#     update_types=update_types.Message,
#     message_types=message_types.Text
# )
# def get_zip_code(bot: TelegramBot, update: Update, state: TelegramState):
#     chat_id = update.get_chat().get_id()
#     message_text = update.get_message().get_text()
#     user_id = update.get_user().get_id()
#
#     if not message_text.isdigit():
#         bot.sendMessage(chat_id, "zip code should be digits")
#     elif len(message_text) == 5:
#         state.update_memory({'ZipCode': message_text})
#
#         data = state.get_memory()
#         product_name = data.get('ProductName')
#         product_price = data.get('ProductPrice')
#         name = data.get('Name')
#         street = data.get('Street')
#         city = data.get('City')
#         state_name = data.get('State')
#         zip_code = data.get('ZipCode')
#
#         add_in_shopping_cart(
#             user_id=user_id,
#             product_name=product_name,
#             product_price=product_price,
#             name=name,
#             street=street,
#             city=city,
#             state=state_name,
#             zip_code=zip_code
#         )
#         state.reset_memory()
#
#         bot.sendMessage(
#             chat_id,
#             'added in shopping cart and wait for pay off',
#         )
#
#         state.set_name('/Home')
#         go_home(chat_id, bot)
#     else:
#         bot.sendMessage(chat_id, f"enter just 5 digit not {len(message_text)}")
