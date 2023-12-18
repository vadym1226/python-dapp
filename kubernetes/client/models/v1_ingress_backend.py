# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.29
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1IngressBackend(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resource': 'V1TypedLocalObjectReference',
        'service': 'V1IngressServiceBackend'
    }

    attribute_map = {
        'resource': 'resource',
        'service': 'service'
    }

    def __init__(self, resource=None, service=None, local_vars_configuration=None):  # noqa: E501
        """V1IngressBackend - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource = None
        self._service = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if service is not None:
            self.service = service

    @property
    def resource(self):
        """Gets the resource of this V1IngressBackend.  # noqa: E501


        :return: The resource of this V1IngressBackend.  # noqa: E501
        :rtype: V1TypedLocalObjectReference
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1IngressBackend.


        :param resource: The resource of this V1IngressBackend.  # noqa: E501
        :type: V1TypedLocalObjectReference
        """

        self._resource = resource

    @property
    def service(self):
        """Gets the service of this V1IngressBackend.  # noqa: E501


        :return: The service of this V1IngressBackend.  # noqa: E501
        :rtype: V1IngressServiceBackend
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this V1IngressBackend.


        :param service: The service of this V1IngressBackend.  # noqa: E501
        :type: V1IngressServiceBackend
        """

        self._service = service

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1IngressBackend):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1IngressBackend):
            return True

        return self.to_dict() != other.to_dict()
