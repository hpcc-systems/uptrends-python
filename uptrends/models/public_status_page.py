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


class PublicStatusPage(object):
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
        'public_dashboard_guid': 'str',
        'name': 'str',
        'is_published': 'bool',
        'preset_period_type': 'PresetPeriodType',
        'customization_info': 'CustomizationInfo',
        'sla_guid': 'str',
        'monitor_guids': 'list[str]',
        'monitor_group_guids': 'list[str]'
    }

    attribute_map = {
        'public_dashboard_guid': 'PublicDashboardGuid',
        'name': 'Name',
        'is_published': 'IsPublished',
        'preset_period_type': 'PresetPeriodType',
        'customization_info': 'CustomizationInfo',
        'sla_guid': 'SlaGuid',
        'monitor_guids': 'MonitorGuids',
        'monitor_group_guids': 'MonitorGroupGuids'
    }

    def __init__(self, public_dashboard_guid=None, name=None, is_published=None, preset_period_type=None, customization_info=None, sla_guid=None, monitor_guids=None, monitor_group_guids=None):  # noqa: E501
        """PublicStatusPage - a model defined in Swagger"""  # noqa: E501

        self._public_dashboard_guid = None
        self._name = None
        self._is_published = None
        self._preset_period_type = None
        self._customization_info = None
        self._sla_guid = None
        self._monitor_guids = None
        self._monitor_group_guids = None
        self.discriminator = None

        if public_dashboard_guid is not None:
            self.public_dashboard_guid = public_dashboard_guid
        if name is not None:
            self.name = name
        if is_published is not None:
            self.is_published = is_published
        if preset_period_type is not None:
            self.preset_period_type = preset_period_type
        if customization_info is not None:
            self.customization_info = customization_info
        if sla_guid is not None:
            self.sla_guid = sla_guid
        if monitor_guids is not None:
            self.monitor_guids = monitor_guids
        if monitor_group_guids is not None:
            self.monitor_group_guids = monitor_group_guids

    @property
    def public_dashboard_guid(self):
        """Gets the public_dashboard_guid of this PublicStatusPage.  # noqa: E501


        :return: The public_dashboard_guid of this PublicStatusPage.  # noqa: E501
        :rtype: str
        """
        return self._public_dashboard_guid

    @public_dashboard_guid.setter
    def public_dashboard_guid(self, public_dashboard_guid):
        """Sets the public_dashboard_guid of this PublicStatusPage.


        :param public_dashboard_guid: The public_dashboard_guid of this PublicStatusPage.  # noqa: E501
        :type: str
        """

        self._public_dashboard_guid = public_dashboard_guid

    @property
    def name(self):
        """Gets the name of this PublicStatusPage.  # noqa: E501


        :return: The name of this PublicStatusPage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicStatusPage.


        :param name: The name of this PublicStatusPage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_published(self):
        """Gets the is_published of this PublicStatusPage.  # noqa: E501


        :return: The is_published of this PublicStatusPage.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this PublicStatusPage.


        :param is_published: The is_published of this PublicStatusPage.  # noqa: E501
        :type: bool
        """

        self._is_published = is_published

    @property
    def preset_period_type(self):
        """Gets the preset_period_type of this PublicStatusPage.  # noqa: E501


        :return: The preset_period_type of this PublicStatusPage.  # noqa: E501
        :rtype: PresetPeriodType
        """
        return self._preset_period_type

    @preset_period_type.setter
    def preset_period_type(self, preset_period_type):
        """Sets the preset_period_type of this PublicStatusPage.


        :param preset_period_type: The preset_period_type of this PublicStatusPage.  # noqa: E501
        :type: PresetPeriodType
        """

        self._preset_period_type = preset_period_type

    @property
    def customization_info(self):
        """Gets the customization_info of this PublicStatusPage.  # noqa: E501


        :return: The customization_info of this PublicStatusPage.  # noqa: E501
        :rtype: CustomizationInfo
        """
        return self._customization_info

    @customization_info.setter
    def customization_info(self, customization_info):
        """Sets the customization_info of this PublicStatusPage.


        :param customization_info: The customization_info of this PublicStatusPage.  # noqa: E501
        :type: CustomizationInfo
        """

        self._customization_info = customization_info

    @property
    def sla_guid(self):
        """Gets the sla_guid of this PublicStatusPage.  # noqa: E501


        :return: The sla_guid of this PublicStatusPage.  # noqa: E501
        :rtype: str
        """
        return self._sla_guid

    @sla_guid.setter
    def sla_guid(self, sla_guid):
        """Sets the sla_guid of this PublicStatusPage.


        :param sla_guid: The sla_guid of this PublicStatusPage.  # noqa: E501
        :type: str
        """

        self._sla_guid = sla_guid

    @property
    def monitor_guids(self):
        """Gets the monitor_guids of this PublicStatusPage.  # noqa: E501


        :return: The monitor_guids of this PublicStatusPage.  # noqa: E501
        :rtype: list[str]
        """
        return self._monitor_guids

    @monitor_guids.setter
    def monitor_guids(self, monitor_guids):
        """Sets the monitor_guids of this PublicStatusPage.


        :param monitor_guids: The monitor_guids of this PublicStatusPage.  # noqa: E501
        :type: list[str]
        """

        self._monitor_guids = monitor_guids

    @property
    def monitor_group_guids(self):
        """Gets the monitor_group_guids of this PublicStatusPage.  # noqa: E501


        :return: The monitor_group_guids of this PublicStatusPage.  # noqa: E501
        :rtype: list[str]
        """
        return self._monitor_group_guids

    @monitor_group_guids.setter
    def monitor_group_guids(self, monitor_group_guids):
        """Sets the monitor_group_guids of this PublicStatusPage.


        :param monitor_group_guids: The monitor_group_guids of this PublicStatusPage.  # noqa: E501
        :type: list[str]
        """

        self._monitor_group_guids = monitor_group_guids

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
        if issubclass(PublicStatusPage, dict):
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
        if not isinstance(other, PublicStatusPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
