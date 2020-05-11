# coding: utf-8

"""
    Uptrends API v4

    This document describes Uptrends API version 4. This Swagger environment also lets you execute API methods directly.  Please note that this is not a sandbox environment: these API methods operate directly on your actual Uptrends account.  For more information, please visit https://www.uptrends.com/api.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import uptrends
from uptrends.api.status_api import StatusApi  # noqa: E501
from uptrends.rest import ApiException


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self):
        self.api = uptrends.api.status_api.StatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_status_get_monitor_group_status(self):
        """Test case for status_get_monitor_group_status

        Gets a list of all monitor group status data.  # noqa: E501
        """
        pass

    def test_status_get_monitor_status(self):
        """Test case for status_get_monitor_status

        Gets all monitor status data.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
