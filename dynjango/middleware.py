from random import random
from django.conf import settings
from django.http import HttpResponse

from .customer_settings import _customer_settings

# New style middleware Django 2.0+
def switch_middleware(get_response):
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
        return response

    return middleware

# Old style middleware
class SwitchMiddleWare(object):
    def process_request(self, request):
        customer_name = request.META.get('HTTP_CUSTOMER', 'default')
        print('\nDOING REQUEST USING {}'.format(customer_name))
        _customer_settings.set_customer(customer_name)

    def process_response(self, request, response):
        return response
