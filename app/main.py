from fastapi import FastAPI

app = FastAPI(
    title="AI Interviewer",
    description="An evidence-based adaptive interview system",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}