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
from uptrends.api.sla_api import SLAApi  # noqa: E501
from uptrends.rest import ApiException


class TestSLAApi(unittest.TestCase):
    """SLAApi unit test stubs"""

    def setUp(self):
        self.api = uptrends.api.sla_api.SLAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sla_create_sla(self):
        """Test case for sla_create_sla

        Creates a new SLA.  # noqa: E501
        """
        pass

    def test_sla_delete_exclusion_period(self):
        """Test case for sla_delete_exclusion_period

        Deletes the specified exclusion period for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_delete_sla(self):
        """Test case for sla_delete_sla

        Deletes the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_get_exclusion_period(self):
        """Test case for sla_get_exclusion_period

        Gets the specified exclusion period for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_get_exclusion_periods(self):
        """Test case for sla_get_exclusion_periods

        Gets a list of all exclusion periods for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_get_sla(self):
        """Test case for sla_get_sla

        Gets the specified SLA definition.  # noqa: E501
        """
        pass

    def test_sla_get_slas(self):
        """Test case for sla_get_slas

        Gets a list of all SLA definitions.  # noqa: E501
        """
        pass

    def test_sla_patch_exclusion_period(self):
        """Test case for sla_patch_exclusion_period

        Partially updates the specified exclusion period for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_patch_sla(self):
        """Test case for sla_patch_sla

        Partially updates the definition of the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_post_exclusion_period(self):
        """Test case for sla_post_exclusion_period

        Creates a new exclusion period for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_put_exclusion_period(self):
        """Test case for sla_put_exclusion_period

        Updates the specified exclusion period for the specified SLA.  # noqa: E501
        """
        pass

    def test_sla_put_sla(self):
        """Test case for sla_put_sla

        Updates the definition of the specified SLA.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
