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
from uptrends.api.register_api import RegisterApi  # noqa: E501
from uptrends.rest import ApiException


class TestRegisterApi(unittest.TestCase):
    """RegisterApi unit test stubs"""

    def setUp(self):
        self.api = uptrends.api.register_api.RegisterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_register_post(self):
        """Test case for register_post

        Creates a new API account.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
