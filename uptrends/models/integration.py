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


class Integration(object):
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
        'integration_guid': 'str',
        'name': 'str',
        'type': 'object',
        'extra_email_addresses': 'str',
        'status_hub_service_list': 'list[IntegrationServiceMap]',
        'integration_services': 'list[str]'
    }

    attribute_map = {
        'integration_guid': 'IntegrationGuid',
        'name': 'Name',
        'type': 'Type',
        'extra_email_addresses': 'ExtraEmailAddresses',
        'status_hub_service_list': 'StatusHubServiceList',
        'integration_services': 'IntegrationServices'
    }

    def __init__(self, integration_guid=None, name=None, type=None, extra_email_addresses=None, status_hub_service_list=None, integration_services=None):  # noqa: E501
        """Integration - a model defined in Swagger"""  # noqa: E501

        self._integration_guid = None
        self._name = None
        self._type = None
        self._extra_email_addresses = None
        self._status_hub_service_list = None
        self._integration_services = None
        self.discriminator = None

        self.integration_guid = integration_guid
        if name is not None:
            self.name = name
        self.type = type
        if extra_email_addresses is not None:
            self.extra_email_addresses = extra_email_addresses
        if status_hub_service_list is not None:
            self.status_hub_service_list = status_hub_service_list
        if integration_services is not None:
            self.integration_services = integration_services

    @property
    def integration_guid(self):
        """Gets the integration_guid of this Integration.  # noqa: E501

        Guid of Integration in Alert Definition Escalation Level  # noqa: E501

        :return: The integration_guid of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._integration_guid

    @integration_guid.setter
    def integration_guid(self, integration_guid):
        """Sets the integration_guid of this Integration.

        Guid of Integration in Alert Definition Escalation Level  # noqa: E501

        :param integration_guid: The integration_guid of this Integration.  # noqa: E501
        :type: str
        """
        if integration_guid is None:
            raise ValueError("Invalid value for `integration_guid`, must not be `None`")  # noqa: E501

        self._integration_guid = integration_guid

    @property
    def name(self):
        """Gets the name of this Integration.  # noqa: E501

        Name of Integration in Alert Definition Escalation Level  # noqa: E501

        :return: The name of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Integration.

        Name of Integration in Alert Definition Escalation Level  # noqa: E501

        :param name: The name of this Integration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Integration.  # noqa: E501

        Type of Integration in Alert Definition Escalation Level  # noqa: E501

        :return: The type of this Integration.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Integration.

        Type of Integration in Alert Definition Escalation Level  # noqa: E501

        :param type: The type of this Integration.  # noqa: E501
        :type: object
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def extra_email_addresses(self):
        """Gets the extra_email_addresses of this Integration.  # noqa: E501

        Extra emailadresses for this integration (if type == email)  # noqa: E501

        :return: The extra_email_addresses of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._extra_email_addresses

    @extra_email_addresses.setter
    def extra_email_addresses(self, extra_email_addresses):
        """Sets the extra_email_addresses of this Integration.

        Extra emailadresses for this integration (if type == email)  # noqa: E501

        :param extra_email_addresses: The extra_email_addresses of this Integration.  # noqa: E501
        :type: str
        """

        self._extra_email_addresses = extra_email_addresses

    @property
    def status_hub_service_list(self):
        """Gets the status_hub_service_list of this Integration.  # noqa: E501

        All statushubs for this integration (if type == statushub)  # noqa: E501

        :return: The status_hub_service_list of this Integration.  # noqa: E501
        :rtype: list[IntegrationServiceMap]
        """
        return self._status_hub_service_list

    @status_hub_service_list.setter
    def status_hub_service_list(self, status_hub_service_list):
        """Sets the status_hub_service_list of this Integration.

        All statushubs for this integration (if type == statushub)  # noqa: E501

        :param status_hub_service_list: The status_hub_service_list of this Integration.  # noqa: E501
        :type: list[IntegrationServiceMap]
        """

        self._status_hub_service_list = status_hub_service_list

    @property
    def integration_services(self):
        """Gets the integration_services of this Integration.  # noqa: E501

        All integrations services.  # noqa: E501

        :return: The integration_services of this Integration.  # noqa: E501
        :rtype: list[str]
        """
        return self._integration_services

    @integration_services.setter
    def integration_services(self, integration_services):
        """Sets the integration_services of this Integration.

        All integrations services.  # noqa: E501

        :param integration_services: The integration_services of this Integration.  # noqa: E501
        :type: list[str]
        """

        self._integration_services = integration_services

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
        if issubclass(Integration, dict):
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
        if not isinstance(other, Integration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
