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
from kubernetes.client.models.apps_v1beta1_deployment_status import AppsV1beta1DeploymentStatus


class TestAppsV1beta1DeploymentStatus(unittest.TestCase):
    """ AppsV1beta1DeploymentStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAppsV1beta1DeploymentStatus(self):
        """
        Test AppsV1beta1DeploymentStatus
        """
        model = kubernetes.client.models.apps_v1beta1_deployment_status.AppsV1beta1DeploymentStatus()


if __name__ == '__main__':
    unittest.main()
