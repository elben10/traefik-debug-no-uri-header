# To deploy

1. docker build -t api --file ./api/Dockerfile .
1. docker network create --driver=overlay traefik-public
1. export `EMAIL=<INSERT EMAIL FOR LETS ENCRYPT>`
1. docker stack deploy -c traefik.yml traefik
1. 
    1. export `TRAEFIK_TAG=traefik-public`
    1. export `TRAEFIK_PUBLIC_TAG=traefik-public`
    1. export `TRAEFIK_PUBLIC_NETWORK=traefik-public` 
    1. export `DOMAIN=<INSERT DOMAIN>` 
    1. export `STACK_NAME=a-stack`
1. docker stack deploy -c docker-compose.yml a-stack

# Credits 

This project is based on https://github.com/tiangolo/full-stack-fastapi-postgresql and dockerswarm.rocks
