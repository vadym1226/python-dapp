# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_storage_class import V1beta1StorageClass


class TestV1beta1StorageClass(unittest.TestCase):
    """ V1beta1StorageClass unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1StorageClass(self):
        """
        Test V1beta1StorageClass
        """
        model = kubernetes.client.models.v1beta1_storage_class.V1beta1StorageClass()


if __name__ == '__main__':
    unittest.main()
