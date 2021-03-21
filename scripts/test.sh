docker rm -f toy_dev
docker rm -f toy1_api-service_1
docker rm -f toy1_nginx_1

bash ./log_generator/build_and_run.sh
docker-compose build
docker-compose up -d


