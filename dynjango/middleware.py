from random import random
from django.conf import settings
from django.http import HttpResponse

from .customer_settings import _customer_settings
# from django.db import connections

def switch_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # if random() > 0.5:
        #     customer_name = 'test2'
        # else:
        #     customer_name = 'test1'
        customer_name = request.META.get('HTTP_CUSTOMER', 'default')

        print('DOING REQUEST USING', customer_name)


        _customer_settings.set_customer(customer_name)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware