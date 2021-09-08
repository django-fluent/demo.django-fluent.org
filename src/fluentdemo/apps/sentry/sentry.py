import logging

import sentry_sdk
from django.conf import settings
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.redis import RedisIntegration


def init_sentry_sdk():
    """Initialize the sentry SDK"""
    if settings.SENTRY_DSN:
        sentry_sdk.init(
            settings.SENTRY_DSN,
            environment=settings.SENTRY_ENVIRONMENT,
            release=settings.GIT_VERSION,
            integrations=[
                LoggingIntegration(event_level=logging.WARNING),
                DjangoIntegration(transaction_style="function_name"),
                RedisIntegration(),
            ]
        )
