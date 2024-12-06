import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

@app.post("/healthy")
def post_health_check(data: dict):
    return {"status": "Healthy", "received": data}


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
