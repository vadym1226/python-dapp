# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ResourceRequirements(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, limits=None, requests=None):
        """
        V1ResourceRequirements - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limits': 'dict(str, str)',
            'requests': 'dict(str, str)'
        }

        self.attribute_map = {
            'limits': 'limits',
            'requests': 'requests'
        }

        self._limits = limits
        self._requests = requests

    @property
    def limits(self):
        """
        Gets the limits of this V1ResourceRequirements.
        Limits describes the maximum amount of compute resources allowed. More info: http://kubernetes.io/docs/user-guide/compute-resources/

        :return: The limits of this V1ResourceRequirements.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this V1ResourceRequirements.
        Limits describes the maximum amount of compute resources allowed. More info: http://kubernetes.io/docs/user-guide/compute-resources/

        :param limits: The limits of this V1ResourceRequirements.
        :type: dict(str, str)
        """

        self._limits = limits

    @property
    def requests(self):
        """
        Gets the requests of this V1ResourceRequirements.
        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: http://kubernetes.io/docs/user-guide/compute-resources/

        :return: The requests of this V1ResourceRequirements.
        :rtype: dict(str, str)
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """
        Sets the requests of this V1ResourceRequirements.
        Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: http://kubernetes.io/docs/user-guide/compute-resources/

        :param requests: The requests of this V1ResourceRequirements.
        :type: dict(str, str)
        """

        self._requests = requests

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ResourceRequirements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
