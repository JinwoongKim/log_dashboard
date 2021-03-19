import logging
import datetime
import time

# TODO log rotation

logging.basicConfig(filename='./log/example.log', encoding='utf-8', level=logging.INFO)

while True:
    logging.info(datetime.datetime.now())
    time.sleep(60)
