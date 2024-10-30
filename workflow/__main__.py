import uvicorn

from workflow import ROUTERS
from workflow.core import FASTAPI_SETTINGS
from workflow.core.init import init_application


def run_app():
    app = init_application(ROUTERS)

    uvicorn.run(
        app,
        host=FASTAPI_SETTINGS.HOST,
        port=FASTAPI_SETTINGS.PORT,
        log_level="info",
    )


if __name__ == "__main__":
    run_app()
