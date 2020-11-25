from fastapi import FastAPI, Request

app = FastAPI(
    openapi_url="/api/openapi.json"
)

@app.get("/api")
def is_authenticated(request: Request):
    print(request.headers)