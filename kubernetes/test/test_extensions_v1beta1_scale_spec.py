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
from kubernetes.client.models.extensions_v1beta1_scale_spec import ExtensionsV1beta1ScaleSpec


class TestExtensionsV1beta1ScaleSpec(unittest.TestCase):
    """ ExtensionsV1beta1ScaleSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtensionsV1beta1ScaleSpec(self):
        """
        Test ExtensionsV1beta1ScaleSpec
        """
        model = kubernetes.client.models.extensions_v1beta1_scale_spec.ExtensionsV1beta1ScaleSpec()


if __name__ == '__main__':
    unittest.main()
