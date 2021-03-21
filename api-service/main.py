from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1")
def read_test():
	return {"Hello": "Uvicorn World"}

@app.get("/api/v1/jwkim")
def read_jwkim():
	return "Welcome Jinwoong"

@app.get("/api/v1/get_log")
def get_log():
	f = open("./log/example.log","r")
	return f.read()
