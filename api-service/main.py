from fastapi import FastAPI
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

@app.get("/api/v1/{log_name}")
def get_log(log_name:str):
	f = open("./log/{}.log".format(log_name),"r")
	return f.read()
