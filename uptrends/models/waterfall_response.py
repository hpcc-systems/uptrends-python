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


class WaterfallResponse(object):
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
        'attributes': 'WaterfallInfo',
        'id': 'int',
        'type': 'str',
        'relationships': 'list[RelationObject]',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'attributes': 'Attributes',
        'id': 'Id',
        'type': 'Type',
        'relationships': 'Relationships',
        'links': 'Links'
    }

    def __init__(self, attributes=None, id=None, type=None, relationships=None, links=None):  # noqa: E501
        """WaterfallResponse - a model defined in Swagger"""  # noqa: E501

        self._attributes = None
        self._id = None
        self._type = None
        self._relationships = None
        self._links = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        self.id = id
        if type is not None:
            self.type = type
        if relationships is not None:
            self.relationships = relationships
        if links is not None:
            self.links = links

    @property
    def attributes(self):
        """Gets the attributes of this WaterfallResponse.  # noqa: E501


        :return: The attributes of this WaterfallResponse.  # noqa: E501
        :rtype: WaterfallInfo
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this WaterfallResponse.


        :param attributes: The attributes of this WaterfallResponse.  # noqa: E501
        :type: WaterfallInfo
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this WaterfallResponse.  # noqa: E501


        :return: The id of this WaterfallResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WaterfallResponse.


        :param id: The id of this WaterfallResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this WaterfallResponse.  # noqa: E501


        :return: The type of this WaterfallResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WaterfallResponse.


        :param type: The type of this WaterfallResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def relationships(self):
        """Gets the relationships of this WaterfallResponse.  # noqa: E501


        :return: The relationships of this WaterfallResponse.  # noqa: E501
        :rtype: list[RelationObject]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this WaterfallResponse.


        :param relationships: The relationships of this WaterfallResponse.  # noqa: E501
        :type: list[RelationObject]
        """

        self._relationships = relationships

    @property
    def links(self):
        """Gets the links of this WaterfallResponse.  # noqa: E501


        :return: The links of this WaterfallResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WaterfallResponse.


        :param links: The links of this WaterfallResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if issubclass(WaterfallResponse, dict):
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
        if not isinstance(other, WaterfallResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
