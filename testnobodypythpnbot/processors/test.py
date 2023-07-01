from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types

# keyboards
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove

from django_tgbot.types.update import Update
from ..bot import state_manager
from ..models import TelegramState
from ..bot import TelegramBot

from ..credentials import BotName

home_keyabord = ReplyKeyboardMarkup.a([
    [KeyboardButton.a(text='buy credit card')],
    [KeyboardButton.a(text='profile'), KeyboardButton.a(text='contact')]
], resize_keyboard=True)


@processor(
    state_manager,
    from_states=state_types.Reset,
    success='handle_home',
    update_types=update_types.Message,
    message_types=message_types.Text,
)
def start(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    user_id = update.get_user().get_id()
    user_name = update.get_user().get_username()

    bot.sendMessage(chat_id, f"welcome to {BotName} {user_name}"
                             f"\nid: {user_id}", reply_markup=home_keyabord)


@processor(
    state_manager,
    from_states=state_types.Reset,
    success=state_types.Reset,
    exclude_update_types=update_types.Message,
    exclude_message_types=update_types.Message,
)
def start_fail(bot, update, state):
    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, "cant understand your command\nplease enter text")



@processor(
    state_manager,
    from_states='handle_home',
    success=state_types.Reset,
    update_types=update_types.Message,
    message_types=message_types.Text
)
def home_ok(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()

    bot.sendMessage(chat_id,'you send this message')
    bot.sendMessage(chat_id, text,
                    reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
