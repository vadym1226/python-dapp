# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_config_map import V1ConfigMap


class TestV1ConfigMap(unittest.TestCase):
    """ V1ConfigMap unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ConfigMap(self):
        """
        Test V1ConfigMap
        """
        model = kubernetes.client.models.v1_config_map.V1ConfigMap()


if __name__ == '__main__':
    unittest.main()
