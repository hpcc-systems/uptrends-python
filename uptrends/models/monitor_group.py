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


class MonitorGroup(object):
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
        'monitor_group_guid': 'str',
        'description': 'str',
        'is_all': 'bool'
    }

    attribute_map = {
        'monitor_group_guid': 'MonitorGroupGuid',
        'description': 'Description',
        'is_all': 'IsAll'
    }

    def __init__(self, monitor_group_guid=None, description=None, is_all=None):  # noqa: E501
        """MonitorGroup - a model defined in Swagger"""  # noqa: E501

        self._monitor_group_guid = None
        self._description = None
        self._is_all = None
        self.discriminator = None

        self.monitor_group_guid = monitor_group_guid
        if description is not None:
            self.description = description
        self.is_all = is_all

    @property
    def monitor_group_guid(self):
        """Gets the monitor_group_guid of this MonitorGroup.  # noqa: E501

        The unique identifier of this monitor group  # noqa: E501

        :return: The monitor_group_guid of this MonitorGroup.  # noqa: E501
        :rtype: str
        """
        return self._monitor_group_guid

    @monitor_group_guid.setter
    def monitor_group_guid(self, monitor_group_guid):
        """Sets the monitor_group_guid of this MonitorGroup.

        The unique identifier of this monitor group  # noqa: E501

        :param monitor_group_guid: The monitor_group_guid of this MonitorGroup.  # noqa: E501
        :type: str
        """
        if monitor_group_guid is None:
            raise ValueError("Invalid value for `monitor_group_guid`, must not be `None`")  # noqa: E501

        self._monitor_group_guid = monitor_group_guid

    @property
    def description(self):
        """Gets the description of this MonitorGroup.  # noqa: E501

        The descriptive name of this probe group  # noqa: E501

        :return: The description of this MonitorGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MonitorGroup.

        The descriptive name of this probe group  # noqa: E501

        :param description: The description of this MonitorGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_all(self):
        """Gets the is_all of this MonitorGroup.  # noqa: E501

        Indicates whether this is the default group for all probes  # noqa: E501

        :return: The is_all of this MonitorGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        """Sets the is_all of this MonitorGroup.

        Indicates whether this is the default group for all probes  # noqa: E501

        :param is_all: The is_all of this MonitorGroup.  # noqa: E501
        :type: bool
        """
        if is_all is None:
            raise ValueError("Invalid value for `is_all`, must not be `None`")  # noqa: E501

        self._is_all = is_all

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
        if issubclass(MonitorGroup, dict):
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
        if not isinstance(other, MonitorGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
