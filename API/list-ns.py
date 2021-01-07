from kubernetes import client, config

def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    api = client.CoreV1Api()

    print("Listing NS with status :")
    ret = api.list_namespace(watch=False)

    for i in ret.items:
        print("%s\t%s" % ( i.metadata.name , i.status))

if __name__ == '__main__':
    main()