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
from uptrends.api.scheduled_report_api import ScheduledReportApi  # noqa: E501
from uptrends.rest import ApiException


class TestScheduledReportApi(unittest.TestCase):
    """ScheduledReportApi unit test stubs"""

    def setUp(self):
        self.api = uptrends.api.scheduled_report_api.ScheduledReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_scheduled_report_create_scheduled_report(self):
        """Test case for scheduled_report_create_scheduled_report

        Creates a new scheduled report.  # noqa: E501
        """
        pass

    def test_scheduled_report_delete_specified_scheduled_report(self):
        """Test case for scheduled_report_delete_specified_scheduled_report

        Delete the specified scheduled report.  # noqa: E501
        """
        pass

    def test_scheduled_report_get_all_scheduled_reports(self):
        """Test case for scheduled_report_get_all_scheduled_reports

        Returns data for all scheduled reports.  # noqa: E501
        """
        pass

    def test_scheduled_report_get_specified_scheduled_report(self):
        """Test case for scheduled_report_get_specified_scheduled_report

        Returns data for the specified scheduled report.  # noqa: E501
        """
        pass

    def test_scheduled_report_partially_update_scheduled_report(self):
        """Test case for scheduled_report_partially_update_scheduled_report

        Partially update the specified scheduled report.  # noqa: E501
        """
        pass

    def test_scheduled_report_update_scheduled_report(self):
        """Test case for scheduled_report_update_scheduled_report

        Update the specified scheduled report.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
