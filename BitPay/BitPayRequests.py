from requests import post
from json import dumps
from .BitPaySettings import API_URL, API_PAYMENT_PARENT, API_PAYMENT_URL, API_AUTHENTICATION


def make_bit_pay_url(user_id, product_item_id, product_value):
    url = API_URL + 'create_child_product'
    data = {
        'parent_uid': API_PAYMENT_PARENT,
        'product_name': user_id,
        'value': product_value,
        'extra_data': dumps({'product_item_id': dumps(product_item_id)})
    }

    response = post(url, headers=API_AUTHENTICATION, json=data, timeout=10)
    if response.ok:
        response = response.json().get('uid')
        return API_PAYMENT_URL + response
    else:
        return None
