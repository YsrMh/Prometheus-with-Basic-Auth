# Prometheus-with-Basic-Auth
Prometheus deployment with basic authentication.

### Create username/password for basic-auth using OpenSSL Utilities before pushing the application to Cloud Foundry
From a bash terminal issue the following commands to create the '.htpasswd' file:
```bash
sudo sh -c "echo -n '<username>:' >> .htpasswd"
sudo sh -c "openssl passwd -apr1 >> .htpasswd"
```
You can repeat the above process to create additional users. Once a user is created, the app is ready to be deployed.

### Push app to Cloud Foundry
Push command after logging into CF's targeted organization/space:
```bash
cf push 
```
