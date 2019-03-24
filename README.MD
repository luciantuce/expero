Solution:

A docker-compose file that will bring up 5 services: frontend, backend, postgresql, frontend-lb, backend-lb.
The only exported port will be 80 which leads to frontend load balancer.

Steps to deploy:

* Since we don't have a Docker registry the local images should be built for the FE and BE apps.

```bash
   cd expero/devops-deployment-test/backend
   docker build --no-cache -t frontend .
   cd expero/devops-deployment-test/backend
   docker build --no-cache -t backend .
```

* Now that we do have the images locally we can bring up the services
```bash
    cd expero/devops-deployment-test
    docker-compose up -d
```

* After the services are up, we can scale FE and BE apps.
```bash
    docker-compose scale backend=2
    docker-compose scale frontend=2
```

The output for `docker ps` should be something like:
```bash
CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS              PORTS                                      NAMES
1818a26f623f        backend               "python3 -m flask ru…"   3 seconds ago        Up 2 seconds        0.0.0.0:32776->5001/tcp                    devops-deployment-test_backend_2
d253f2443eaf        frontend              "python3 -m flask ru…"   10 seconds ago       Up 9 seconds        0.0.0.0:32775->5000/tcp                    devops-deployment-test_frontend_2
8173df7f58e0        dockercloud/haproxy   "/sbin/tini -- docke…"   About a minute ago   Up About a minute   443/tcp, 0.0.0.0:80->80/tcp, 1936/tcp      devops-deployment-test_frontend-lb_1
005749e78d83        dockercloud/haproxy   "/sbin/tini -- docke…"   About a minute ago   Up About a minute   443/tcp, 1936/tcp, 0.0.0.0:32774->80/tcp   devops-deployment-test_backend-lb_1
4f5b32490732        postgres              "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp                                   devops-deployment-test_postgresql_1
ff2586274844        frontend              "python3 -m flask ru…"   About a minute ago   Up About a minute   0.0.0.0:32773->5000/tcp                    devops-deployment-test_frontend_1
5a7020d88efe        backend               "python3 -m flask ru…"   About a minute ago   Up About a minute   0.0.0.0:32772->5001/tcp                    devops-deployment-test_backend_1
```

It can be killed any frontend/backend container and the apps will still function.