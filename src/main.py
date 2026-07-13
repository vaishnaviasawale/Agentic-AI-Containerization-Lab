from fastapi import FastAPI

from src.agent import execute

app = FastAPI(title="Orchestrator Agent")


@app.get("/")
def root():

    return {
        "status": "running"
    }


@app.get("/execute")
def run(task: str):

    return execute(task)