# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_persistent_volume_claim import V1PersistentVolumeClaim  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PersistentVolumeClaim(unittest.TestCase):
    """V1PersistentVolumeClaim unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PersistentVolumeClaim
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_persistent_volume_claim.V1PersistentVolumeClaim()  # noqa: E501
        if include_optional :
            return V1PersistentVolumeClaim(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    cluster_name = '0', 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        '0'
                        ], 
                    generate_name = '0', 
                    generation = 56, 
                    labels = {
                        'key' : '0'
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '0', 
                            fields_type = '0', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '0', 
                            operation = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '0', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '0', 
                            name = '0', 
                            uid = '0', )
                        ], 
                    resource_version = '0', 
                    self_link = '0', 
                    uid = '0', ), 
                spec = kubernetes.client.models.v1/persistent_volume_claim_spec.v1.PersistentVolumeClaimSpec(
                    access_modes = [
                        '0'
                        ], 
                    data_source = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '0', 
                        kind = '0', 
                        name = '0', ), 
                    resources = kubernetes.client.models.v1/resource_requirements.v1.ResourceRequirements(
                        limits = {
                            'key' : '0'
                            }, 
                        requests = {
                            'key' : '0'
                            }, ), 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '0', 
                                operator = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, ), 
                    storage_class_name = '0', 
                    volume_mode = '0', 
                    volume_name = '0', ), 
                status = kubernetes.client.models.v1/persistent_volume_claim_status.v1.PersistentVolumeClaimStatus(
                    access_modes = [
                        '0'
                        ], 
                    capacity = {
                        'key' : '0'
                        }, 
                    conditions = [
                        kubernetes.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                            last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    phase = '0', )
            )
        else :
            return V1PersistentVolumeClaim(
        )

    def testV1PersistentVolumeClaim(self):
        """Test V1PersistentVolumeClaim"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
