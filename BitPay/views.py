from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .BitPayHook import bit_pay_get_hook, bit_pay_make_new, bit_pay_update

from CardManager.CardManagerRequest import make_virtual_card


# from testnobodypythpnbot.processors.BotPayment import send_pay_status


# Create your views here.

def bit_pay_main_hook(request):
    if request.GET:

        address = request.GET.get('addr')
        status = request.GET.get('status')
        if (address is None) or (status is None):
            return HttpResponseNotFound(request)

        response = bit_pay_get_hook(address)
        if not response:
            return HttpResponseNotFound(request)

        if response.get('status') == 0:
            bit_pay_make_new(response)
            return HttpResponse(request, 'OK')

        elif response.get('status') in [1, 2]:
            bit_pay_update(response)
            return HttpResponse(request, 'OK')

        elif response.get('status') in [-2, -1]:
            # fail
            return HttpResponse(request, 'OK')

    # return HttpResponse(request, "OK")
    return HttpResponseNotFound(request)
