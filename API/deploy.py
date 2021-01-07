from os import path
from kubernetes import client, config
import yaml
yaml.load(input, Loader=yaml.FullLoader)

def main():
    #configs if not args provided , the config will be loaded from default location
    config.load_kube_config()

    with open(path.join(path.dirname(__file__),'nginx-deployment.yaml')) as f:

        dep = yaml.load(f)
        k8s = client.AppsV1Api()
        status = k8s_beta.create_namespaced_deployment (
            body=dep, namespace="default").status
        print ("Deployment created. status='{}'".format(status))

if __name__ == '__main__':
    main()