# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_daemon_set_spec import V1beta1DaemonSetSpec


class TestV1beta1DaemonSetSpec(unittest.TestCase):
    """ V1beta1DaemonSetSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1DaemonSetSpec(self):
        """
        Test V1beta1DaemonSetSpec
        """
        model = kubernetes.client.models.v1beta1_daemon_set_spec.V1beta1DaemonSetSpec()


if __name__ == '__main__':
    unittest.main()
