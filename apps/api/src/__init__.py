import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import agents, api_keys, api_provider
from src.routers import auth as auth_router
from src.routers import (
    billing_information,
    crews,
    index,
    messages,
    profiles,
    rest,
    sandbox,
    sessions,
    subscriptions,
    tiers,
    tools,
)


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(index.router)
    app.include_router(sessions.router)
    app.include_router(messages.router)
    app.include_router(crews.router)
    app.include_router(agents.router)
    app.include_router(profiles.router)
    app.include_router(api_keys.router)
    app.include_router(auth_router.router)
    app.include_router(api_provider.router)
    app.include_router(tools.router)
    app.include_router(subscriptions.router)
    app.include_router(rest.router)
    app.include_router(tiers.router)
    app.include_router(billing_information.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://localhost:5174",
            "http://localhost:8000",
            "http://localhost:8001",
            "http://localhost:8080",
            "http://localhost:8081",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:5174",
            "http://127.0.0.1:8000",
            "http://127.0.0.1:8001",
            "http://127.0.0.1:8080",
            "http://127.0.0.1:8081",
            "https://aiti.no",
            "https://api.aiti.no",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

def run():
    app = create_app()
    sandbox_app = sandbox.create_app()
    app.mount("/sandbox", sandbox_app)

    uvicorn.run(app, host="0.0.0.0", port=8000, log_config="logging.yaml")


if __name__ == "__main__":
    run()
