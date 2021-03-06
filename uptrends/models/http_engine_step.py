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


class HttpEngineStep(object):
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
        'step_name': 'str',
        'url': 'str',
        'http_status_code': 'str',
        'http_method': 'str',
        'http_status_description': 'str',
        'response_completed': 'bool',
        'step_executed': 'bool',
        'assertion_results_info': 'object',
        'total_time': 'int',
        'response_headers': 'str',
        'response_body': 'str',
        'request_headers': 'str',
        'request_body': 'str'
    }

    attribute_map = {
        'step_name': 'StepName',
        'url': 'Url',
        'http_status_code': 'HttpStatusCode',
        'http_method': 'HttpMethod',
        'http_status_description': 'HttpStatusDescription',
        'response_completed': 'ResponseCompleted',
        'step_executed': 'StepExecuted',
        'assertion_results_info': 'AssertionResultsInfo',
        'total_time': 'TotalTime',
        'response_headers': 'ResponseHeaders',
        'response_body': 'ResponseBody',
        'request_headers': 'RequestHeaders',
        'request_body': 'RequestBody'
    }

    def __init__(self, step_name=None, url=None, http_status_code=None, http_method=None, http_status_description=None, response_completed=None, step_executed=None, assertion_results_info=None, total_time=None, response_headers=None, response_body=None, request_headers=None, request_body=None):  # noqa: E501
        """HttpEngineStep - a model defined in Swagger"""  # noqa: E501

        self._step_name = None
        self._url = None
        self._http_status_code = None
        self._http_method = None
        self._http_status_description = None
        self._response_completed = None
        self._step_executed = None
        self._assertion_results_info = None
        self._total_time = None
        self._response_headers = None
        self._response_body = None
        self._request_headers = None
        self._request_body = None
        self.discriminator = None

        if step_name is not None:
            self.step_name = step_name
        if url is not None:
            self.url = url
        if http_status_code is not None:
            self.http_status_code = http_status_code
        if http_method is not None:
            self.http_method = http_method
        if http_status_description is not None:
            self.http_status_description = http_status_description
        self.response_completed = response_completed
        self.step_executed = step_executed
        if assertion_results_info is not None:
            self.assertion_results_info = assertion_results_info
        self.total_time = total_time
        if response_headers is not None:
            self.response_headers = response_headers
        if response_body is not None:
            self.response_body = response_body
        if request_headers is not None:
            self.request_headers = request_headers
        if request_body is not None:
            self.request_body = request_body

    @property
    def step_name(self):
        """Gets the step_name of this HttpEngineStep.  # noqa: E501

        The name of the step  # noqa: E501

        :return: The step_name of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this HttpEngineStep.

        The name of the step  # noqa: E501

        :param step_name: The step_name of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._step_name = step_name

    @property
    def url(self):
        """Gets the url of this HttpEngineStep.  # noqa: E501

        Url the step was executed on  # noqa: E501

        :return: The url of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HttpEngineStep.

        Url the step was executed on  # noqa: E501

        :param url: The url of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def http_status_code(self):
        """Gets the http_status_code of this HttpEngineStep.  # noqa: E501

        The HTTP status code returned  # noqa: E501

        :return: The http_status_code of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this HttpEngineStep.

        The HTTP status code returned  # noqa: E501

        :param http_status_code: The http_status_code of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._http_status_code = http_status_code

    @property
    def http_method(self):
        """Gets the http_method of this HttpEngineStep.  # noqa: E501

        Http method used in this step  # noqa: E501

        :return: The http_method of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this HttpEngineStep.

        Http method used in this step  # noqa: E501

        :param http_method: The http_method of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._http_method = http_method

    @property
    def http_status_description(self):
        """Gets the http_status_description of this HttpEngineStep.  # noqa: E501

        Step description  # noqa: E501

        :return: The http_status_description of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._http_status_description

    @http_status_description.setter
    def http_status_description(self, http_status_description):
        """Sets the http_status_description of this HttpEngineStep.

        Step description  # noqa: E501

        :param http_status_description: The http_status_description of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._http_status_description = http_status_description

    @property
    def response_completed(self):
        """Gets the response_completed of this HttpEngineStep.  # noqa: E501

        Did the response complete?  # noqa: E501

        :return: The response_completed of this HttpEngineStep.  # noqa: E501
        :rtype: bool
        """
        return self._response_completed

    @response_completed.setter
    def response_completed(self, response_completed):
        """Sets the response_completed of this HttpEngineStep.

        Did the response complete?  # noqa: E501

        :param response_completed: The response_completed of this HttpEngineStep.  # noqa: E501
        :type: bool
        """
        if response_completed is None:
            raise ValueError("Invalid value for `response_completed`, must not be `None`")  # noqa: E501

        self._response_completed = response_completed

    @property
    def step_executed(self):
        """Gets the step_executed of this HttpEngineStep.  # noqa: E501

        Was this step executed?  # noqa: E501

        :return: The step_executed of this HttpEngineStep.  # noqa: E501
        :rtype: bool
        """
        return self._step_executed

    @step_executed.setter
    def step_executed(self, step_executed):
        """Sets the step_executed of this HttpEngineStep.

        Was this step executed?  # noqa: E501

        :param step_executed: The step_executed of this HttpEngineStep.  # noqa: E501
        :type: bool
        """
        if step_executed is None:
            raise ValueError("Invalid value for `step_executed`, must not be `None`")  # noqa: E501

        self._step_executed = step_executed

    @property
    def assertion_results_info(self):
        """Gets the assertion_results_info of this HttpEngineStep.  # noqa: E501

        Results of the assertions in this step  # noqa: E501

        :return: The assertion_results_info of this HttpEngineStep.  # noqa: E501
        :rtype: object
        """
        return self._assertion_results_info

    @assertion_results_info.setter
    def assertion_results_info(self, assertion_results_info):
        """Sets the assertion_results_info of this HttpEngineStep.

        Results of the assertions in this step  # noqa: E501

        :param assertion_results_info: The assertion_results_info of this HttpEngineStep.  # noqa: E501
        :type: object
        """

        self._assertion_results_info = assertion_results_info

    @property
    def total_time(self):
        """Gets the total_time of this HttpEngineStep.  # noqa: E501

        Number of milliseconds it took for this step to succeed  # noqa: E501

        :return: The total_time of this HttpEngineStep.  # noqa: E501
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this HttpEngineStep.

        Number of milliseconds it took for this step to succeed  # noqa: E501

        :param total_time: The total_time of this HttpEngineStep.  # noqa: E501
        :type: int
        """
        if total_time is None:
            raise ValueError("Invalid value for `total_time`, must not be `None`")  # noqa: E501

        self._total_time = total_time

    @property
    def response_headers(self):
        """Gets the response_headers of this HttpEngineStep.  # noqa: E501

        Response headers  # noqa: E501

        :return: The response_headers of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this HttpEngineStep.

        Response headers  # noqa: E501

        :param response_headers: The response_headers of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._response_headers = response_headers

    @property
    def response_body(self):
        """Gets the response_body of this HttpEngineStep.  # noqa: E501

        Response body  # noqa: E501

        :return: The response_body of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this HttpEngineStep.

        Response body  # noqa: E501

        :param response_body: The response_body of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._response_body = response_body

    @property
    def request_headers(self):
        """Gets the request_headers of this HttpEngineStep.  # noqa: E501

        Request headers send  # noqa: E501

        :return: The request_headers of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this HttpEngineStep.

        Request headers send  # noqa: E501

        :param request_headers: The request_headers of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._request_headers = request_headers

    @property
    def request_body(self):
        """Gets the request_body of this HttpEngineStep.  # noqa: E501

        Request body send  # noqa: E501

        :return: The request_body of this HttpEngineStep.  # noqa: E501
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this HttpEngineStep.

        Request body send  # noqa: E501

        :param request_body: The request_body of this HttpEngineStep.  # noqa: E501
        :type: str
        """

        self._request_body = request_body

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
        if issubclass(HttpEngineStep, dict):
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
        if not isinstance(other, HttpEngineStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
