# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: release-1.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1NodeDaemonEndpoints(object):
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
        'kubelet_endpoint': 'V1DaemonEndpoint'
    }

    attribute_map = {
        'kubelet_endpoint': 'kubeletEndpoint'
    }

    def __init__(self, kubelet_endpoint=None):  # noqa: E501
        """V1NodeDaemonEndpoints - a model defined in OpenAPI"""  # noqa: E501

        self._kubelet_endpoint = None
        self.discriminator = None

        if kubelet_endpoint is not None:
            self.kubelet_endpoint = kubelet_endpoint

    @property
    def kubelet_endpoint(self):
        """Gets the kubelet_endpoint of this V1NodeDaemonEndpoints.  # noqa: E501


        :return: The kubelet_endpoint of this V1NodeDaemonEndpoints.  # noqa: E501
        :rtype: V1DaemonEndpoint
        """
        return self._kubelet_endpoint

    @kubelet_endpoint.setter
    def kubelet_endpoint(self, kubelet_endpoint):
        """Sets the kubelet_endpoint of this V1NodeDaemonEndpoints.


        :param kubelet_endpoint: The kubelet_endpoint of this V1NodeDaemonEndpoints.  # noqa: E501
        :type: V1DaemonEndpoint
        """

        self._kubelet_endpoint = kubelet_endpoint

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
        if not isinstance(other, V1NodeDaemonEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
