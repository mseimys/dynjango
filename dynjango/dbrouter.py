from .customer_settings import _customer_settings

class CustomerRouter(object):
    def db_for_read(self, model, **hints):
        return _customer_settings.database

    def db_for_write(self, model, **hints):
        return _customer_settings.database
