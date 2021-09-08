from django.apps import AppConfig

from .sentry import init_sentry_sdk


class BaseAppConfig(AppConfig):
    name = 'fluentdemo.apps.sentry'

    def ready(self):
        """
        Monkey patch after apps are loaded.
        """
        # Moved SDK initialization to ready() moment,
        # so SENTRY_DSN can be redefined by other setting files.
        init_sentry_sdk()
