# coding: utf-8

"""
    Uptrends API v4

    This document describes Uptrends API version 4. This Swagger environment also lets you execute API methods directly.  Please note that this is not a sandbox environment: these API methods operate directly on your actual Uptrends account.  For more information, please visit https://www.uptrends.com/api.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MonitorQuota(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'basic_monitors': 'int',
        'basic_monitors_in_use': 'int',
        'browser_monitors': 'int',
        'browser_monitors_in_use': 'int',
        'api_monitoring_credits': 'int',
        'api_monitoring_credits_in_use': 'int',
        'transaction_credits': 'int',
        'transaction_credits_in_use': 'int',
        'monitors': 'int',
        'monitors_in_use': 'int'
    }

    attribute_map = {
        'basic_monitors': 'BasicMonitors',
        'basic_monitors_in_use': 'BasicMonitorsInUse',
        'browser_monitors': 'BrowserMonitors',
        'browser_monitors_in_use': 'BrowserMonitorsInUse',
        'api_monitoring_credits': 'ApiMonitoringCredits',
        'api_monitoring_credits_in_use': 'ApiMonitoringCreditsInUse',
        'transaction_credits': 'TransactionCredits',
        'transaction_credits_in_use': 'TransactionCreditsInUse',
        'monitors': 'Monitors',
        'monitors_in_use': 'MonitorsInUse'
    }

    def __init__(self, basic_monitors=None, basic_monitors_in_use=None, browser_monitors=None, browser_monitors_in_use=None, api_monitoring_credits=None, api_monitoring_credits_in_use=None, transaction_credits=None, transaction_credits_in_use=None, monitors=None, monitors_in_use=None):  # noqa: E501
        """MonitorQuota - a model defined in Swagger"""  # noqa: E501

        self._basic_monitors = None
        self._basic_monitors_in_use = None
        self._browser_monitors = None
        self._browser_monitors_in_use = None
        self._api_monitoring_credits = None
        self._api_monitoring_credits_in_use = None
        self._transaction_credits = None
        self._transaction_credits_in_use = None
        self._monitors = None
        self._monitors_in_use = None
        self.discriminator = None

        if basic_monitors is not None:
            self.basic_monitors = basic_monitors
        if basic_monitors_in_use is not None:
            self.basic_monitors_in_use = basic_monitors_in_use
        if browser_monitors is not None:
            self.browser_monitors = browser_monitors
        if browser_monitors_in_use is not None:
            self.browser_monitors_in_use = browser_monitors_in_use
        if api_monitoring_credits is not None:
            self.api_monitoring_credits = api_monitoring_credits
        if api_monitoring_credits_in_use is not None:
            self.api_monitoring_credits_in_use = api_monitoring_credits_in_use
        if transaction_credits is not None:
            self.transaction_credits = transaction_credits
        if transaction_credits_in_use is not None:
            self.transaction_credits_in_use = transaction_credits_in_use
        if monitors is not None:
            self.monitors = monitors
        if monitors_in_use is not None:
            self.monitors_in_use = monitors_in_use

    @property
    def basic_monitors(self):
        """Gets the basic_monitors of this MonitorQuota.  # noqa: E501


        :return: The basic_monitors of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._basic_monitors

    @basic_monitors.setter
    def basic_monitors(self, basic_monitors):
        """Sets the basic_monitors of this MonitorQuota.


        :param basic_monitors: The basic_monitors of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._basic_monitors = basic_monitors

    @property
    def basic_monitors_in_use(self):
        """Gets the basic_monitors_in_use of this MonitorQuota.  # noqa: E501


        :return: The basic_monitors_in_use of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._basic_monitors_in_use

    @basic_monitors_in_use.setter
    def basic_monitors_in_use(self, basic_monitors_in_use):
        """Sets the basic_monitors_in_use of this MonitorQuota.


        :param basic_monitors_in_use: The basic_monitors_in_use of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._basic_monitors_in_use = basic_monitors_in_use

    @property
    def browser_monitors(self):
        """Gets the browser_monitors of this MonitorQuota.  # noqa: E501


        :return: The browser_monitors of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._browser_monitors

    @browser_monitors.setter
    def browser_monitors(self, browser_monitors):
        """Sets the browser_monitors of this MonitorQuota.


        :param browser_monitors: The browser_monitors of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._browser_monitors = browser_monitors

    @property
    def browser_monitors_in_use(self):
        """Gets the browser_monitors_in_use of this MonitorQuota.  # noqa: E501


        :return: The browser_monitors_in_use of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._browser_monitors_in_use

    @browser_monitors_in_use.setter
    def browser_monitors_in_use(self, browser_monitors_in_use):
        """Sets the browser_monitors_in_use of this MonitorQuota.


        :param browser_monitors_in_use: The browser_monitors_in_use of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._browser_monitors_in_use = browser_monitors_in_use

    @property
    def api_monitoring_credits(self):
        """Gets the api_monitoring_credits of this MonitorQuota.  # noqa: E501


        :return: The api_monitoring_credits of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._api_monitoring_credits

    @api_monitoring_credits.setter
    def api_monitoring_credits(self, api_monitoring_credits):
        """Sets the api_monitoring_credits of this MonitorQuota.


        :param api_monitoring_credits: The api_monitoring_credits of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._api_monitoring_credits = api_monitoring_credits

    @property
    def api_monitoring_credits_in_use(self):
        """Gets the api_monitoring_credits_in_use of this MonitorQuota.  # noqa: E501


        :return: The api_monitoring_credits_in_use of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._api_monitoring_credits_in_use

    @api_monitoring_credits_in_use.setter
    def api_monitoring_credits_in_use(self, api_monitoring_credits_in_use):
        """Sets the api_monitoring_credits_in_use of this MonitorQuota.


        :param api_monitoring_credits_in_use: The api_monitoring_credits_in_use of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._api_monitoring_credits_in_use = api_monitoring_credits_in_use

    @property
    def transaction_credits(self):
        """Gets the transaction_credits of this MonitorQuota.  # noqa: E501


        :return: The transaction_credits of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._transaction_credits

    @transaction_credits.setter
    def transaction_credits(self, transaction_credits):
        """Sets the transaction_credits of this MonitorQuota.


        :param transaction_credits: The transaction_credits of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._transaction_credits = transaction_credits

    @property
    def transaction_credits_in_use(self):
        """Gets the transaction_credits_in_use of this MonitorQuota.  # noqa: E501


        :return: The transaction_credits_in_use of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._transaction_credits_in_use

    @transaction_credits_in_use.setter
    def transaction_credits_in_use(self, transaction_credits_in_use):
        """Sets the transaction_credits_in_use of this MonitorQuota.


        :param transaction_credits_in_use: The transaction_credits_in_use of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._transaction_credits_in_use = transaction_credits_in_use

    @property
    def monitors(self):
        """Gets the monitors of this MonitorQuota.  # noqa: E501


        :return: The monitors of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this MonitorQuota.


        :param monitors: The monitors of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._monitors = monitors

    @property
    def monitors_in_use(self):
        """Gets the monitors_in_use of this MonitorQuota.  # noqa: E501


        :return: The monitors_in_use of this MonitorQuota.  # noqa: E501
        :rtype: int
        """
        return self._monitors_in_use

    @monitors_in_use.setter
    def monitors_in_use(self, monitors_in_use):
        """Sets the monitors_in_use of this MonitorQuota.


        :param monitors_in_use: The monitors_in_use of this MonitorQuota.  # noqa: E501
        :type: int
        """

        self._monitors_in_use = monitors_in_use

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MonitorQuota, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MonitorQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
