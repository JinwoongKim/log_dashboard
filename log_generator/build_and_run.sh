mkdir -p log
docker rm -f toy_dev
docker build . -t dev
docker run -v /Users/jwkim/github/toy1/log_generator/log:/home/jwkim/log --name toy_dev -dt dev
