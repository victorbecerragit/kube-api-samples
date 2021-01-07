from kubernetes import client, config , watch

#to test in remote cluster use this
#config.load_incluster_config()

def main():
    # Config can be set in conf class directly or using helper utility
    # to test locally use this
    config.load_kube_config()
    api = client.CoreV1Api()

    #v1 = client.CoreV1Api()
    count = 10
    w = watch.Watch()

    for event in w.stream(api.list_namespace, _request_timeout=30):
        print (f"Event: {event['type']} {event['object'].metadata.name}")
        count -= 1
        print (count)

        if count == 0:
            print('Done.')
            w.stop()

if __name__ == '__main__':
    main()