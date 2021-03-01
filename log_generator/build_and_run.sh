docker rm -f toy_dev
docker build . -t dev
docker run --name toy_dev -dt dev
