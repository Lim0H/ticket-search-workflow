import uvicorn
from fastapi import FastAPI

from workflow.core import FASTAPI_SETTINGS
from workflow.core.init import init_application

init_application()
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=FASTAPI_SETTINGS.HOST,
        port=FASTAPI_SETTINGS.PORT,
        log_level="info",
    )
