from kubernetes import client, config

def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    apps_api = client.AppsV1Api()

    print("Listing deployments by namespace (default):")
    ret = apps_api.list_namespaced_deployment(namespace="default")

    for i in ret.items:
        print("%s" % ( i.metadata.name ))

if __name__ == '__main__':
    main()
