from .models import ShoppingCart, Card
from testnobodypythpnbot.models import TelegramUser
from .CardManagerSettings import rave


def add_in_shopping_cart(user_id, product_name, product_value, product_price, name):
    user = TelegramUser.object.search_user_id(user_id=user_id)
    if not user:
        return False

    ShoppingCart.object.create(
        UserID=user,
        ItemID=ShoppingCart.object.get_next_item_id(user_id=user_id),
        ProductName=product_name,
        ProductValue=product_value,
        ProductPrice=product_price,
        Name=name
    )
    return True


def make_virtual_card(user_id, items):
    for item in items:
        cart = ShoppingCart.object.get_by_user_id_and_item_id(user_id, item)
        if not cart:
            continue

        res = rave.VirtualCard.create({
            "currency": "USD",
            "amount": cart.ProductValue if cart.ProductValue != 5 else 1,
            "billing_name": cart.Name,
            "billing_address": 'Providence Street',
            "billing_city": 'Lekki',
            "billing_state": 'Lagos',
            "billing_postal_code": '12345',
            "billing_country": "US"
        })

        if cart.ProductValue == 1 or cart.ProductValue == '1':
            rave.VirtualCard.withdraw({
                'id': res.get('id'),
                'amount': 4
            })

        res = res.get('data')
        Card.object.create(
            UserID=cart.UserID,
            CardID=res.get('id'),
            # City=res.get('city'),
            # State=res.get('state'),
            # Address=res.get('address_1'),
            # ZipCode=res.get('zip_code'),
            # CardPan=res.get('card_pan'),
            # CVV=res.get('cvv'),
            # Expiration=res.get('expiration'),
            # Name=res.get('name_on_card'),
            # Amount=res.get('amount')
        )

        ShoppingCart.object.remove_by_item_id(user_id, item)
