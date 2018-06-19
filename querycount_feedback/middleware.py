# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

try:
    from querycount.qc_settings import QC_SETTINGS
except ImportError:
    raise ImproperlyConfigured('Unable to import querycount QC_SETTINGS. Do you have "django-querycount" installed & configured?')


HEAD_SNIPPET = """
    <style>
    body {
        border: 10px solid %s;
    }
    </style>
"""

class QueryCountFeedbackMiddleware(MiddlewareMixin):
    """This middleware adds an orange resp. red border to the html if
    `MEDIUM` or `HIGH` threshold is reached.
    """

    def __init__(self, *args, **kwargs):
        super(QueryCountFeedbackMiddleware, self).__init__(*args, **kwargs)

        if settings.DEBUG:
            self.threshold = QC_SETTINGS['THRESHOLDS']



    def _ignore_request(self, path):
        """Check to see if we should ignore the request."""
        return any([
            re.match(pattern, path) for pattern in QC_SETTINGS['IGNORE_REQUEST_PATTERNS']
        ])


    def _get_count_from_header(self, response):

        try:
            return int(response[QC_SETTINGS['RESPONSE_HEADER']])

        except BaseException as e:
            # TODO: catch only relevant exceptions
            pass


    def process_response(self, request, response):

        if settings.DEBUG and not self._ignore_request(request.path):

            _count = self._get_count_from_header(response)
            if _count and _count > self.threshold['MEDIUM']:

                _color = 'red' if _count >= self.threshold['HIGH'] else 'orange'
                _snippet = HEAD_SNIPPET % _color

                try:
                    response.content = response.content.replace(
                        b'</head>', bytes(_snippet.encode('utf-8')) + b'\n</head>'
                    )

                except BaseException as e:
                    # TODO: catch only relevant exceptions
                    pass

        return response
