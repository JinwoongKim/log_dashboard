FROM python:3.9.2

RUN apt-get update -y
RUN apt-get install -y vim

RUN useradd -ms /bin/bash jwkim
WORKDIR /home/jwkim

COPY main.py .
COPY get_log.sh .

RUN chown jwkim:jwkim get_log.sh
RUN chown jwkim:jwkim main.py
RUN chmod +x get_log.sh

USER jwkim


ENTRYPOINT ["python","main.py"]
