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
from uptrends.api.operator_group_api import OperatorGroupApi  # noqa: E501
from uptrends.rest import ApiException


class TestOperatorGroupApi(unittest.TestCase):
    """OperatorGroupApi unit test stubs"""

    def setUp(self):
        self.api = uptrends.api.operator_group_api.OperatorGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_operator_group_add_duty_schedule_to_all_members(self):
        """Test case for operator_group_add_duty_schedule_to_all_members

        Adds the provided duty schedule to all operators in the group specified   # noqa: E501
        """
        pass

    def test_operator_group_add_operator_to_operator_group(self):
        """Test case for operator_group_add_operator_to_operator_group

        Adds the specified operator to the operator group   # noqa: E501
        """
        pass

    def test_operator_group_all_operators_in_group_off_duty(self):
        """Test case for operator_group_all_operators_in_group_off_duty

        Set the OnDuty flag to off for all operators that are a member of the operator group specified by the operator group GUID  # noqa: E501
        """
        pass

    def test_operator_group_all_operators_in_group_on_duty(self):
        """Test case for operator_group_all_operators_in_group_on_duty

        Set the OnDuty flag to on for all operators that are a member of the operator group specified by the operator group GUID  # noqa: E501
        """
        pass

    def test_operator_group_create_operator_group(self):
        """Test case for operator_group_create_operator_group

        Creates a new operator group  # noqa: E501
        """
        pass

    def test_operator_group_delete_operator_group(self):
        """Test case for operator_group_delete_operator_group

        Deletes the specified operator group  # noqa: E501
        """
        pass

    def test_operator_group_get_all_operator_groups(self):
        """Test case for operator_group_get_all_operator_groups

        Gets all operator groups  # noqa: E501
        """
        pass

    def test_operator_group_get_operator_group(self):
        """Test case for operator_group_get_operator_group

        Gets the details of a operator group  # noqa: E501
        """
        pass

    def test_operator_group_get_operator_group_members(self):
        """Test case for operator_group_get_operator_group_members

        Gets a list of all members of an operator group  # noqa: E501
        """
        pass

    def test_operator_group_remove_operator_from_operator_group(self):
        """Test case for operator_group_remove_operator_from_operator_group

        Removes the specified operator from the operator group  # noqa: E501
        """
        pass

    def test_operator_group_update_operator_group(self):
        """Test case for operator_group_update_operator_group

        Updates the operator group with the Guid specified  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()