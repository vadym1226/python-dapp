# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1VolumeAttachmentSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'persistent_volume_name': 'str'
    }

    attribute_map = {
        'persistent_volume_name': 'persistentVolumeName'
    }

    def __init__(self, persistent_volume_name=None):
        """
        V1alpha1VolumeAttachmentSource - a model defined in Swagger
        """

        self._persistent_volume_name = None
        self.discriminator = None

        if persistent_volume_name is not None:
          self.persistent_volume_name = persistent_volume_name

    @property
    def persistent_volume_name(self):
        """
        Gets the persistent_volume_name of this V1alpha1VolumeAttachmentSource.
        Name of the persistent volume to attach.

        :return: The persistent_volume_name of this V1alpha1VolumeAttachmentSource.
        :rtype: str
        """
        return self._persistent_volume_name

    @persistent_volume_name.setter
    def persistent_volume_name(self, persistent_volume_name):
        """
        Sets the persistent_volume_name of this V1alpha1VolumeAttachmentSource.
        Name of the persistent volume to attach.

        :param persistent_volume_name: The persistent_volume_name of this V1alpha1VolumeAttachmentSource.
        :type: str
        """

        self._persistent_volume_name = persistent_volume_name

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
        if not isinstance(other, V1alpha1VolumeAttachmentSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
