from kubernetes import client, config
 
node_name = "minikube-m03" 

def main(node_name):

     # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    api = client.CoreV1Api()

    # Deletes a kubernetes node from the cluster
    configuration = client.Configuration()
    # create an instance of the API class
    k8s_api = client.CoreV1Api(client.ApiClient(configuration))
    print ("Deleting k8s node {}...".format(node_name))
    #try:
     #   if not app_config['DRY_RUN']:
            # k8s_api.delete_node(minikube-m03)
            api.delete_node()

      #  else:
       #     k8s_api.delete_node(node_name, dry_run="true")
        print ("Node deleted")
    except ApiException as e:
        print ("Exception when calling CoreV1Api->delete_node: {}".format(e)) 

if __name__ == '__main__':
    main()