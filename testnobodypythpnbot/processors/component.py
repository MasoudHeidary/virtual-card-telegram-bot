from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.inlinekeyboardbutton import InlineKeyboardButton

# from django_tgbot.state_manager import state_types

# -------------------------------------------------------------------------- Home
# home keyboard
HomeKeyboard = ReplyKeyboardMarkup.a(keyboard=[
    [KeyboardButton.a(text='Order Virtual Card')],
    [KeyboardButton.a(text='Shopping Cart')],
    [KeyboardButton.a(text='My Cards')],
    [KeyboardButton.a(text='FAQs'), KeyboardButton.a(text='Contact Admin')],
], resize_keyboard=True, one_time_keyboard=True)

# back Home keyboard
BackHomeKeyboard = ReplyKeyboardMarkup.a(keyboard=[
    [KeyboardButton.a(text='Home')]
], resize_keyboard=True, one_time_keyboard=True)

# -------------------------------------------------------------------------- Buy
BuyCardOptionKeyboard = ReplyKeyboardMarkup.a(keyboard=[
    [KeyboardButton.a(text='USA Virtual Debit Card'), KeyboardButton.a(text='PayPal Verification Card(4.99$)')],
    [KeyboardButton.a(text='Home')]
], resize_keyboard=True, one_time_keyboard=True)

# BuyCard inline keyboard ,return card(name,value,cost)
BuyCardCostKeyboard = InlineKeyboardMarkup.a(inline_keyboard=[
    [InlineKeyboardButton.a(text='5$(7.99$)', callback_data='5$ virtual card,5,7.99'),
     InlineKeyboardButton.a(text='10$(13.99$)', callback_data='10$ virtual card,10,13.99')],
    [InlineKeyboardButton.a(text='20$(25.49$)', callback_data='20$ virtual card,20,25.49'),
     InlineKeyboardButton.a(text='30$(36.99$)', callback_data='30$ virtual card,30,36.99')],
    [InlineKeyboardButton.a(text='40$(48.99$)', callback_data='40$ virtual card,40,48.99'),
     InlineKeyboardButton.a(text='50$(59.99$)', callback_data='50$ virtual card,50,59.99')],
    [InlineKeyboardButton.a(text='75$(86.99$)', callback_data='75$ virtual card,75,86.99'),
     InlineKeyboardButton.a(text='100$(119.99$)', callback_data='100$ virtual card,100,119.99')],
    [InlineKeyboardButton.a(text='150$(175.99$)', callback_data='150$ virtual card,150,175.99'),
     InlineKeyboardButton.a(text='200$(229.99$)', callback_data='200$ virtual card,200,229.99')],
])


# -------------------------------------------------------------------------- shopping cart
def shopping_cart_keyboard(amount):
    return ReplyKeyboardMarkup.a(keyboard=[
        [KeyboardButton.a(text=f"Your Invoice {amount}$")],
        [KeyboardButton.a(text='Home')]
    ], resize_keyboard=True, one_time_keyboard=True)


def shopping_cart_remove_inline_keyboard(item_id):
    return InlineKeyboardMarkup.a(inline_keyboard=[
        [InlineKeyboardButton.a(text='Remove this item', callback_data=f'{item_id}')]
    ])

# state inline keyboard
# StateNames = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
#               'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
#               'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
#               'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
#               'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
#               'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
#               'Wisconsin', 'Wyoming']
#
# StateWords = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
#               'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
#               'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


# def make_paged_state_keyboard(start, end, next=True, previous=True):
#     k = [[InlineKeyboardButton.a(text=StateNames[i], callback_data=StateWords[i]),
#           InlineKeyboardButton.a(text=StateNames[i + 1], callback_data=StateWords[i + 1])]
#          for i in range(start, end, 2)]
#     page = []
#     if previous:
#         page += [InlineKeyboardButton.a(text='<-- Prev', callback_data='/PrevPage')]
#     if next:
#         page += [InlineKeyboardButton.a(text='Next -->', callback_data='/NextPage')]
#
#     k += [page]
#     return k


# StateKeyboard_1 = InlineKeyboardMarkup.a(inline_keyboard=make_paged_state_keyboard(0, 10, previous=False))
# StateKeyboard_2 = InlineKeyboardMarkup.a(inline_keyboard=make_paged_state_keyboard(10, 20))
# StateKeyboard_3 = InlineKeyboardMarkup.a(inline_keyboard=make_paged_state_keyboard(20, 30))
# StateKeyboard_4 = InlineKeyboardMarkup.a(inline_keyboard=make_paged_state_keyboard(30, 40))
# StateKeyboard_5 = InlineKeyboardMarkup.a(inline_keyboard=make_paged_state_keyboard(40, 50, next=False))
# StateKeyboard = [StateKeyboard_1, StateKeyboard_2, StateKeyboard_3, StateKeyboard_4, StateKeyboard_5]
