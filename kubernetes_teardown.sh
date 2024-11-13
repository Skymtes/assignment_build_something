# kubectl delete --cascade='foreground' -f .\list_service\list_service_deployment.yml
# kubectl delete --cascade='foreground' -f .\upload_service\upload_service_deployment.yml
# kubectl delete --cascade='foreground' -f .\root_service\root_service_deployment.yml
# kubectl delete --cascade='foreground' -f .\cassandra_deployment.yml

kubectl delete --cascade='foreground' -f .\complete_deployment.yml 
