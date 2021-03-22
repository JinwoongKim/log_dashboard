from fastapi import FastAPI
from typing import Optional

from watchlist import watchlist

app = FastAPI()

@app.get("/api/v1")
def read_test():
	return {"Hello": "Uvicorn World"}

@app.get("/api/v1/jwkim")
def read_jwkim():
	return "Welcome Jinwoong"

@app.get("/api/v1/watchlist")
def get_watchlist():
	return watchlist

@app.get("/api/v1/services")
def services():
	return [{"name":"serviceName1", "status":"OK"},
            {"name":"serviceName2", "status":"ERROR"}]

@app.get("/api/v1/service/{name}")
def service(name:str, level:Optional[str]=None, date:Optional[str]=None):
	return "service name: {}, level: {}, date: {}".format(name, level, date)

@app.get("/api/v1/{log_name}")
def get_log(log_name:str):
	f = open("./log/{}.log".format(log_name),"r")
	return f.read()
