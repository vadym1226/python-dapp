# Copyright 2021 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This example demonstrates the following:
    - Creation of a namespaced scoped custom resource definition (CRD) using dynamic-client
    - Creation of custom resources (CR) using the above created CRD
    - List, patch(update), delete the custom resources
    - Delete the custom resource defintion
"""

from kubernetes import config, dynamic
from kubernetes.dynamic.exceptions import ResourceNotFoundError
from kubernetes.client import api_client
import time


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the custom resource definition (CRD) api
    crd_api = client.resources.get(
        api_version="apiextensions.k8s.io/v1beta1", kind="CustomResourceDefinition"
    )

    # Creating a Namespaced CRD named "ingressroutes.apps.example.com"
    name = "ingressroutes.apps.example.com"

    crd_manifest = {
        "apiVersion": "apiextensions.k8s.io/v1beta1",
        "kind": "CustomResourceDefinition",
        "metadata": {
            "name": name,
            "namespace": "default",
        },
        "spec": {
            "group": "apps.example.com",
            "names": {
                "kind": "IngressRoute",
                "listKind": "IngressRouteList",
                "plural": "ingressroutes",
                "singular": "ingressroute",
            },
            "scope": "Namespaced",
            "version": "v1",
            "subresources": {"status": {}},
        },
    }

    crd_creation_respone = crd_api.create(crd_manifest)
    print(
        "\n[INFO] custom resource definition `ingressroutes.apps.example.com` created\n"
    )
    print("%s\t\t%s" % ("SCOPE", "NAME"))
    print(
        "%s\t%s\n"
        % (crd_creation_respone.spec.scope, crd_creation_respone.metadata.name)
    )

    # Fetching the "ingressroutes" CRD api

    try:
        ingressroute_api = client.resources.get(
            api_version="apps.example.com/v1", kind="IngressRoute"
        )
    except ResourceNotFoundError:
        # Need to wait a sec for the discovery layer to get updated
        time.sleep(2)

    ingressroute_api = client.resources.get(
        api_version="apps.example.com/v1", kind="IngressRoute"
    )

    # Creating a custom resource (CR) `ingress-route-*`, using the above CRD `ingressroutes.apps.example.com`

    ingressroute_manifest_one = {
        "apiVersion": "apps.example.com/v1",
        "kind": "IngressRoute",
        "metadata": {
            "name": "ingress-route-one",
            "namespace": "default",
        },
        "spec": {},
    }

    ingressroute_manifest_second = {
        "apiVersion": "apps.example.com/v1",
        "kind": "IngressRoute",
        "metadata": {
            "name": "ingress-route-second",
            "namespace": "default",
        },
        "spec": {},
    }

    ingressroute_api.create(body=ingressroute_manifest_one, namespace="default")
    ingressroute_api.create(body=ingressroute_manifest_second, namespace="default")
    print("\n[INFO] custom resources `ingress-route-*` created\n")

    # Listing the `ingress-route-*` custom resources

    ingress_routes_list = ingressroute_api.get()
    print("%s\t\t\t\t%s\t%s" % ("NAME", "NAMESPACE", "SPEC"))
    for item in ingress_routes_list.items:
        print(
            "%s\t\t%s\t\t%s" % (item.metadata.name, item.metadata.namespace, item.spec)
        )

    # Patching the ingressroutes custom resources

    ingressroute_manifest_one["spec"]["entrypoints"] = ["websecure"]
    ingressroute_manifest_second["spec"]["entrypoints"] = ["web"]

    patch_ingressroute_one = ingressroute_api.patch(
        body=ingressroute_manifest_one, content_type="application/merge-patch+json"
    )
    patch_ingressroute_second = ingressroute_api.patch(
        body=ingressroute_manifest_second, content_type="application/merge-patch+json"
    )

    print("\n[INFO] custom resources `ingress-route-*` patched\n")
    patched_ingress_routes_list = ingressroute_api.get()
    print("%s\t\t\t\t%s\t%s" % ("NAME", "NAMESPACE", "SPEC"))
    for item in patched_ingress_routes_list.items:
        print(
            "%s\t\t%s\t\t%s"
            % (item.metadata.name, item.metadata.namespace, str(item.spec))
        )

    # Deleting the ingressroutes custom resources

    delete_ingressroute_one = ingressroute_api.delete(
        name="ingress-route-one", namespace="default"
    )
    delete_ingressroute_second = ingressroute_api.delete(
        name="ingress-route-second", namespace="default"
    )

    print("\n[INFO] custom resources `ingress-route-*` deleted")

    # Deleting the ingressroutes.apps.example.com custom resource definition

    crd_api.delete(name=name)
    print(
        "\n[INFO] custom resource definition `ingressroutes.apps.example.com` deleted"
    )


if __name__ == "__main__":
    main()
