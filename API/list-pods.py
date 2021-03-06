from kubernetes import client, config

def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    api = client.CoreV1Api()

    print("Listing pods with their IPs:")
    ret = api.list_pod_for_all_namespaces(watch=False)

    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

if __name__ == '__main__':
    main()