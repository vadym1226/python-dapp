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
from kubernetes.client.models.v1alpha1_admission_hook_client_config import V1alpha1AdmissionHookClientConfig


class TestV1alpha1AdmissionHookClientConfig(unittest.TestCase):
    """ V1alpha1AdmissionHookClientConfig unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1AdmissionHookClientConfig(self):
        """
        Test V1alpha1AdmissionHookClientConfig
        """
        model = kubernetes.client.models.v1alpha1_admission_hook_client_config.V1alpha1AdmissionHookClientConfig()


if __name__ == '__main__':
    unittest.main()
