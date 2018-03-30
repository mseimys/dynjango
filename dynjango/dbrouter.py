from .customer_settings import _customer_settings

class CustomerRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        return _customer_settings.database

    def db_for_write(self, model, **hints):
        return _customer_settings.database
