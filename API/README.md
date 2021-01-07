# Creating a pod via Kube API

curl -X POST -H "Content-Type: application/json" -d@nginx-pod.json http://localhost:8080/api/v1/namespaces/default/pods

# Deleting a pod via Kube API

curl -X DELETE http://localhost:8080/api/v1/namespaces/default/pods/nginx

# List All deployments

curl -X GET http://localhost:8080/apis/apps/v1/deployments | jq .items[].metadata.name

# List deployments by namespace

curl -s -X GET http://localhost:8080/apis/apps/v1/namespaces/kube-system/deployments | jq .items[].metadata.name

curl -s -X GET http://localhost:8080/apis/apps/v1/namespaces/default/deployments | jq .items[].metadata.name

# Create a deployment via Kube API

curl -X POST -H "Content-Type: application/json" -d@deployment.json http://localhost:8080/apis/apps/v1/namespaces/default/deployments


# nginx-pod.json
{
    "kind": "Pod",
    "apiVersion": "v1",
    "metadata": {
        "name" : "nginx",
        "namespace" : "default",
        "labels" : {
            "name" : "nginx"
        }
    },
    "spec": {
        "containers": [{
            "name" : "nginx",
            "image" : "nginx",
            "ports" : [{"containerPort" : 80}]
        }]
    }
}
