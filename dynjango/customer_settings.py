import threading
from uuid import uuid4

from django.db import connections

class CustomerSettings(threading.local):
    def __init__(self):
        self.database = 'default'

    def set_customer(self, name):
        self.database = str(uuid4())
        connections.databases[self.database] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': name,
        }

_customer_settings = CustomerSettings()
# The CustomerSettings class is no more needed, so remove it from the namespace.
del CustomerSettings
