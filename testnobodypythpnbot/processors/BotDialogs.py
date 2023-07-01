from ..bot import TelegramBot

from .component import HomeKeyboard, BuyCardOptionKeyboard, BuyCardCostKeyboard, shopping_cart_keyboard, \
    shopping_cart_remove_inline_keyboard, BackHomeKeyboard

from CardManager.models import ShoppingCart, Card
from BitPay.BitPayRequests import make_bit_pay_url
from CardManager.CardManagerSettings import rave


def go_home(chat_id, bot: TelegramBot):
    bot.sendMessage(chat_id, "first page", reply_markup=HomeKeyboard)


def join_channel(chat_id, user_id, bot: TelegramBot):
    user_status_in_channel = bot.getChatMember(chat_id='@DaraCard', user_id=user_id)
    if user_status_in_channel.status == 'left':
        bot.sendMessage(chat_id, 'kindly join the channel to order your virtual card \n@DaraCard', reply_markup=HomeKeyboard)
        return False
    return True


# ------------------------------------------------------------------------- Buy

def go_buy_card_option(chat_id, bot: TelegramBot):
    bot.sendMessage(chat_id, 'select your type of card', reply_markup=BuyCardOptionKeyboard)


def go_buy_card(chat_id, bot: TelegramBot):
    bot.sendMessage(chat_id, 'Select the loaded amount', reply_markup=BuyCardCostKeyboard)


def go_shopping_cart(chat_id, user_id, bot: TelegramBot):
    cart = ShoppingCart.object.get_by_user_id(user_id)
    if not cart:
        bot.sendMessage(chat_id, "you haven't ordered any cards")
        return False
    else:
        bill = 0
        count = 0
        for i in cart:
            bot.sendMessage(
                chat_id,
                f"product: {i.ProductName}    Price: {i.ProductPrice}\n"
                f"Name: {i.Name}",
                reply_markup=shopping_cart_remove_inline_keyboard(i.ItemID)
            )
            bill += i.ProductPrice
            count += 1
        bot.sendMessage(chat_id, f'{count} cards in shopping cart', reply_markup=shopping_cart_keyboard(bill))
        return True


# ------------------------------------------------------------------------- UserDetail
def go_get_name(chat_id, bot: TelegramBot):
    message = "Enter the cardholder name:"
    bot.sendMessage(chat_id, message, reply_markup=BackHomeKeyboard)


# def go_get_street(chat_id, bot: TelegramBot):
#     message = "Enter the desired street address: \nlike 471 mundet pl"
#     bot.sendMessage(chat_id, message, reply_markup=BackHomeKeyboard)
#
#
# def go_get_city(chat_id, bot: TelegramBot):
#     message = "Enter the name of the city of your choice: \nlike Hillside"
#     bot.sendMessage(chat_id, message, reply_markup=BackHomeKeyboard)
#
#
# def go_get_state(chat_id, bot: TelegramBot, state: TelegramState):
#     message = "Select the name of the States of your choice:"
#     state.update_memory({'state_page': 0})
#     bot.sendMessage(chat_id, message, reply_markup=StateKeyboard[0])
#
#
# def go_get_zip_code(chat_id, bot: TelegramBot):
#     message = "Enter 5 digits zip code:\nlike 12345"
#     bot.sendMessage(chat_id, message, reply_markup=BackHomeKeyboard)


# ------------------------------------------------------------------------- Payment

def go_pay_off(chat_id, user_id, bot: TelegramBot):
    bill = 0
    items = list()
    cart = ShoppingCart.object.get_by_user_id(user_id=user_id)
    if not cart:
        bot.sendMessage(chat_id, "you haven't ordered any cards", reply_markup=shopping_cart_keyboard(bill))
        return
    for i in cart:
        bill += i.ProductPrice
        items += [i.ItemID]
    url = make_bit_pay_url(user_id, items, float(bill))
    message = f"your invoice:\n{url}"
    bot.sendMessage(chat_id, message, parse_mode='HTML')


# ---------------------------------------------------------

def go_my_card(chat_id, user_id, bot: TelegramBot):
    cards = Card.object.get_by_user_id(user_id)
    if not cards:
        bot.sendMessage("you don't have any cards")
        return

    for card in cards:
        res = rave.VirtualCard.get(card_id=card.CardID)
        res = res.get('returnedData').get('data')
        amount = res.get('amount')
        cardpan = res.get('card_pan')
        city = res.get('city')
        state = res.get('state')
        address = res.get('address_1')
        zip_code = res.get('zip_code')
        cvv = res.get('cvv')
        expiration = res.get('expiration')
        card_type = res.get('card_type')
        name_on_card = res.get('name_on_card')

        message = f"{cardpan} {card_type} {amount}$\n" \
                  f"{expiration}    cvv:{cvv}\n" \
                  f"{name_on_card}    {address} {city} {state} {zip_code}"

        bot.sendMessage(chat_id, message)
