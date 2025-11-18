"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "20251118.0"

PACKAGE_NAME = "tredf.site"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
