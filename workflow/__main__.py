import uvicorn
from fastapi import FastAPI

from workflow.core import FASTAPI_SETTINGS
from workflow.core.init import init_application


def run_app():
    init_application()
    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"Hello": "World"}

    uvicorn.run(
        app,
        host=FASTAPI_SETTINGS.HOST,
        port=FASTAPI_SETTINGS.PORT,
        log_level="info",
    )


if __name__ == "__main__":
    run_app()
