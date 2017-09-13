from django.apps import AppConfig


class RettiwtConfig(AppConfig):
    name = 'rettiwt'

    def ready(self):
        import rettiwt.signals
