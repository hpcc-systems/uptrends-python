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


class AlertDefinition(object):
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
        'alert_definition_guid': 'str',
        'hash': 'str',
        'alert_name': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'alert_definition_guid': 'AlertDefinitionGuid',
        'hash': 'Hash',
        'alert_name': 'AlertName',
        'is_active': 'IsActive'
    }

    def __init__(self, alert_definition_guid=None, hash=None, alert_name=None, is_active=None):  # noqa: E501
        """AlertDefinition - a model defined in Swagger"""  # noqa: E501

        self._alert_definition_guid = None
        self._hash = None
        self._alert_name = None
        self._is_active = None
        self.discriminator = None

        if alert_definition_guid is not None:
            self.alert_definition_guid = alert_definition_guid
        if hash is not None:
            self.hash = hash
        if alert_name is not None:
            self.alert_name = alert_name
        if is_active is not None:
            self.is_active = is_active

    @property
    def alert_definition_guid(self):
        """Gets the alert_definition_guid of this AlertDefinition.  # noqa: E501

        The unique key of this Alert Definition.  # noqa: E501

        :return: The alert_definition_guid of this AlertDefinition.  # noqa: E501
        :rtype: str
        """
        return self._alert_definition_guid

    @alert_definition_guid.setter
    def alert_definition_guid(self, alert_definition_guid):
        """Sets the alert_definition_guid of this AlertDefinition.

        The unique key of this Alert Definition.  # noqa: E501

        :param alert_definition_guid: The alert_definition_guid of this AlertDefinition.  # noqa: E501
        :type: str
        """

        self._alert_definition_guid = alert_definition_guid

    @property
    def hash(self):
        """Gets the hash of this AlertDefinition.  # noqa: E501

        Hash corresponding with this alert definition.  # noqa: E501

        :return: The hash of this AlertDefinition.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this AlertDefinition.

        Hash corresponding with this alert definition.  # noqa: E501

        :param hash: The hash of this AlertDefinition.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def alert_name(self):
        """Gets the alert_name of this AlertDefinition.  # noqa: E501

        Name of this Alert Definition.  # noqa: E501

        :return: The alert_name of this AlertDefinition.  # noqa: E501
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        """Sets the alert_name of this AlertDefinition.

        Name of this Alert Definition.  # noqa: E501

        :param alert_name: The alert_name of this AlertDefinition.  # noqa: E501
        :type: str
        """

        self._alert_name = alert_name

    @property
    def is_active(self):
        """Gets the is_active of this AlertDefinition.  # noqa: E501

        Indicates whether this Alert Definition is active.  # noqa: E501

        :return: The is_active of this AlertDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AlertDefinition.

        Indicates whether this Alert Definition is active.  # noqa: E501

        :param is_active: The is_active of this AlertDefinition.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(AlertDefinition, dict):
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
        if not isinstance(other, AlertDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
