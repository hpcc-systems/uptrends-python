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


class TransactionStep(object):
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
        'step_number': 'int',
        'step_name': 'str',
        'total_time': 'float',
        'elements': 'list[str]',
        'has_error': 'bool'
    }

    attribute_map = {
        'step_number': 'StepNumber',
        'step_name': 'StepName',
        'total_time': 'TotalTime',
        'elements': 'Elements',
        'has_error': 'HasError'
    }

    def __init__(self, step_number=None, step_name=None, total_time=None, elements=None, has_error=None):  # noqa: E501
        """TransactionStep - a model defined in Swagger"""  # noqa: E501

        self._step_number = None
        self._step_name = None
        self._total_time = None
        self._elements = None
        self._has_error = None
        self.discriminator = None

        self.step_number = step_number
        if step_name is not None:
            self.step_name = step_name
        self.total_time = total_time
        if elements is not None:
            self.elements = elements
        self.has_error = has_error

    @property
    def step_number(self):
        """Gets the step_number of this TransactionStep.  # noqa: E501

        Step (index) number  # noqa: E501

        :return: The step_number of this TransactionStep.  # noqa: E501
        :rtype: int
        """
        return self._step_number

    @step_number.setter
    def step_number(self, step_number):
        """Sets the step_number of this TransactionStep.

        Step (index) number  # noqa: E501

        :param step_number: The step_number of this TransactionStep.  # noqa: E501
        :type: int
        """
        if step_number is None:
            raise ValueError("Invalid value for `step_number`, must not be `None`")  # noqa: E501

        self._step_number = step_number

    @property
    def step_name(self):
        """Gets the step_name of this TransactionStep.  # noqa: E501

        The name of the step  # noqa: E501

        :return: The step_name of this TransactionStep.  # noqa: E501
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this TransactionStep.

        The name of the step  # noqa: E501

        :param step_name: The step_name of this TransactionStep.  # noqa: E501
        :type: str
        """

        self._step_name = step_name

    @property
    def total_time(self):
        """Gets the total_time of this TransactionStep.  # noqa: E501

        Number of milliseconds it took for this step to succeed  # noqa: E501

        :return: The total_time of this TransactionStep.  # noqa: E501
        :rtype: float
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this TransactionStep.

        Number of milliseconds it took for this step to succeed  # noqa: E501

        :param total_time: The total_time of this TransactionStep.  # noqa: E501
        :type: float
        """
        if total_time is None:
            raise ValueError("Invalid value for `total_time`, must not be `None`")  # noqa: E501

        self._total_time = total_time

    @property
    def elements(self):
        """Gets the elements of this TransactionStep.  # noqa: E501

        Text representation of the step element results  # noqa: E501

        :return: The elements of this TransactionStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this TransactionStep.

        Text representation of the step element results  # noqa: E501

        :param elements: The elements of this TransactionStep.  # noqa: E501
        :type: list[str]
        """

        self._elements = elements

    @property
    def has_error(self):
        """Gets the has_error of this TransactionStep.  # noqa: E501

        Did this step result in an error?  # noqa: E501

        :return: The has_error of this TransactionStep.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this TransactionStep.

        Did this step result in an error?  # noqa: E501

        :param has_error: The has_error of this TransactionStep.  # noqa: E501
        :type: bool
        """
        if has_error is None:
            raise ValueError("Invalid value for `has_error`, must not be `None`")  # noqa: E501

        self._has_error = has_error

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
        if issubclass(TransactionStep, dict):
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
        if not isinstance(other, TransactionStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
