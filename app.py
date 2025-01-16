from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers.tasks_router import router as tasks_router

app = FastAPI(
    title="Task List API",
    description="API for managing tasks",
    version="1.0.0",
)

app.include_router(tasks_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
