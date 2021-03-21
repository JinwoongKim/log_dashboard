docker rm -f toy1_api-service_1
docker rm -f toy1_nginx_1
docker-compose build
docker-compose up -d
docker exec -it toy1_api-service_1 bash


