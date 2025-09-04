from fastapi import FastAPI

app = FastAPI(title="Template Service", version="0.1.0")


@app.get("/")
def root():
    return {
        "service": "template",
        "status": "ok",
        "message": "Service is running. Implement SPEC.md features here.",
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}

