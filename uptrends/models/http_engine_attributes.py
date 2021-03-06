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


class HttpEngineAttributes(object):
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
        'step_results': 'list[HttpEngineStep]',
        'timing_info': 'object',
        'total_steps': 'int',
        'passed_steps': 'int'
    }

    attribute_map = {
        'step_results': 'StepResults',
        'timing_info': 'TimingInfo',
        'total_steps': 'TotalSteps',
        'passed_steps': 'PassedSteps'
    }

    def __init__(self, step_results=None, timing_info=None, total_steps=None, passed_steps=None):  # noqa: E501
        """HttpEngineAttributes - a model defined in Swagger"""  # noqa: E501

        self._step_results = None
        self._timing_info = None
        self._total_steps = None
        self._passed_steps = None
        self.discriminator = None

        if step_results is not None:
            self.step_results = step_results
        if timing_info is not None:
            self.timing_info = timing_info
        self.total_steps = total_steps
        self.passed_steps = passed_steps

    @property
    def step_results(self):
        """Gets the step_results of this HttpEngineAttributes.  # noqa: E501

        The results of the steps   # noqa: E501

        :return: The step_results of this HttpEngineAttributes.  # noqa: E501
        :rtype: list[HttpEngineStep]
        """
        return self._step_results

    @step_results.setter
    def step_results(self, step_results):
        """Sets the step_results of this HttpEngineAttributes.

        The results of the steps   # noqa: E501

        :param step_results: The step_results of this HttpEngineAttributes.  # noqa: E501
        :type: list[HttpEngineStep]
        """

        self._step_results = step_results

    @property
    def timing_info(self):
        """Gets the timing_info of this HttpEngineAttributes.  # noqa: E501

        Timing info  # noqa: E501

        :return: The timing_info of this HttpEngineAttributes.  # noqa: E501
        :rtype: object
        """
        return self._timing_info

    @timing_info.setter
    def timing_info(self, timing_info):
        """Sets the timing_info of this HttpEngineAttributes.

        Timing info  # noqa: E501

        :param timing_info: The timing_info of this HttpEngineAttributes.  # noqa: E501
        :type: object
        """

        self._timing_info = timing_info

    @property
    def total_steps(self):
        """Gets the total_steps of this HttpEngineAttributes.  # noqa: E501

        Number of total steps  # noqa: E501

        :return: The total_steps of this HttpEngineAttributes.  # noqa: E501
        :rtype: int
        """
        return self._total_steps

    @total_steps.setter
    def total_steps(self, total_steps):
        """Sets the total_steps of this HttpEngineAttributes.

        Number of total steps  # noqa: E501

        :param total_steps: The total_steps of this HttpEngineAttributes.  # noqa: E501
        :type: int
        """
        if total_steps is None:
            raise ValueError("Invalid value for `total_steps`, must not be `None`")  # noqa: E501

        self._total_steps = total_steps

    @property
    def passed_steps(self):
        """Gets the passed_steps of this HttpEngineAttributes.  # noqa: E501

        Number of passed/succeed tests  # noqa: E501

        :return: The passed_steps of this HttpEngineAttributes.  # noqa: E501
        :rtype: int
        """
        return self._passed_steps

    @passed_steps.setter
    def passed_steps(self, passed_steps):
        """Sets the passed_steps of this HttpEngineAttributes.

        Number of passed/succeed tests  # noqa: E501

        :param passed_steps: The passed_steps of this HttpEngineAttributes.  # noqa: E501
        :type: int
        """
        if passed_steps is None:
            raise ValueError("Invalid value for `passed_steps`, must not be `None`")  # noqa: E501

        self._passed_steps = passed_steps

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
        if issubclass(HttpEngineAttributes, dict):
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
        if not isinstance(other, HttpEngineAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
