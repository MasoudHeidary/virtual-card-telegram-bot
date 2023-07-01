from requests import get
from json import loads

from testnobodypythpnbot.models import TelegramUser
from .BitPaySettings import API_URL, API_TOKEN, API_AUTHENTICATION
from .models import BitPayment

from CardManager.CardManagerRequest import make_virtual_card


def bit_pay_get_hook(address):
    url = API_URL + 'merchant_order/' + address
    response = get(url, headers=API_AUTHENTICATION)
    if response.ok:
        return response.json()
    else:
        return False


def bit_pay_make_new(response):
    user_id = response.get('name')
    address = response.get('address')

    # check present in database
    if BitPayment.object.get_by_address(address):
        return False
    else:
        user = TelegramUser.object.get_by_user_id(user_id)
        if not user:
            return False
        BitPayment.object.create(
            UserID=user,
            USD=response.get('value'),
            Satoshi=response.get('satoshi'),
            PaidSatoshi=response.get('paid_satoshi'),
            Status=response.get('status'),
            Time=response.get('timestamp'),
            TXID=response.get('txid'),
            Address=response.get('address'),
            ProductItem=loads(response.get('data').get('extradata')).get('product_item_id')
        )
        return True


def bit_pay_update(response):
    address = response.get('address')
    new_status = response.get('status')

    payment = BitPayment.object.get_by_address(address)
    if not payment:
        return False
    elif payment.Status in [-2, -1]:
        return False

    payment = payment
    current_status = payment.Status

    if current_status >= new_status:
        return False

    payment.PaidSatoshi = response.get('paid_satoshi')
    payment.Status = new_status
    payment.TXID = response.get('txid')
    payment.save()

    # add to user cards
    if new_status == 2:
        make_virtual_card(payment.UserID.telegram_id, loads(payment.ProductItem))

    return True


def bit_pay_fail(response):
    address = response.get('address')
    fail_status = response.get('status')
    if fail_status not in [-2, -1]:
        return False

    payment = BitPayment.object.get_by_address(address)
    if not payment:
        return False

    payment = payment.first()
    payment.PaidSatoshi = response.get('paid_satoshi')
    payment.Status = fail_status
    payment.TXID = response.get('txid')
    payment.save()
    return True
