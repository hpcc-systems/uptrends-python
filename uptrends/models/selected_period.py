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


class SelectedPeriod(object):
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
        'selected_period_type': 'object',
        'start': 'datetime',
        'end': 'datetime',
        'preset_period': 'object'
    }

    attribute_map = {
        'selected_period_type': 'SelectedPeriodType',
        'start': 'Start',
        'end': 'End',
        'preset_period': 'PresetPeriod'
    }

    def __init__(self, selected_period_type=None, start=None, end=None, preset_period=None):  # noqa: E501
        """SelectedPeriod - a model defined in Swagger"""  # noqa: E501

        self._selected_period_type = None
        self._start = None
        self._end = None
        self._preset_period = None
        self.discriminator = None

        if selected_period_type is not None:
            self.selected_period_type = selected_period_type
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if preset_period is not None:
            self.preset_period = preset_period

    @property
    def selected_period_type(self):
        """Gets the selected_period_type of this SelectedPeriod.  # noqa: E501

        The type of period  # noqa: E501

        :return: The selected_period_type of this SelectedPeriod.  # noqa: E501
        :rtype: object
        """
        return self._selected_period_type

    @selected_period_type.setter
    def selected_period_type(self, selected_period_type):
        """Sets the selected_period_type of this SelectedPeriod.

        The type of period  # noqa: E501

        :param selected_period_type: The selected_period_type of this SelectedPeriod.  # noqa: E501
        :type: object
        """

        self._selected_period_type = selected_period_type

    @property
    def start(self):
        """Gets the start of this SelectedPeriod.  # noqa: E501

        The start of a custom period (can't be used together with the SelectedPeriodType parameter)  # noqa: E501

        :return: The start of this SelectedPeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SelectedPeriod.

        The start of a custom period (can't be used together with the SelectedPeriodType parameter)  # noqa: E501

        :param start: The start of this SelectedPeriod.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this SelectedPeriod.  # noqa: E501

        The end of a custom period  # noqa: E501

        :return: The end of this SelectedPeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SelectedPeriod.

        The end of a custom period  # noqa: E501

        :param end: The end of this SelectedPeriod.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def preset_period(self):
        """Gets the preset_period of this SelectedPeriod.  # noqa: E501

        The requested time period.  # noqa: E501

        :return: The preset_period of this SelectedPeriod.  # noqa: E501
        :rtype: object
        """
        return self._preset_period

    @preset_period.setter
    def preset_period(self, preset_period):
        """Sets the preset_period of this SelectedPeriod.

        The requested time period.  # noqa: E501

        :param preset_period: The preset_period of this SelectedPeriod.  # noqa: E501
        :type: object
        """

        self._preset_period = preset_period

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
        if issubclass(SelectedPeriod, dict):
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
        if not isinstance(other, SelectedPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
