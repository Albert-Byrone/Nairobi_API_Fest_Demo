import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# Conditional import due to pytest which imports tests as external packages.
if __name__ in ["__main__", "main"]:
    from msingi_app_backend.api.projects.route import router as project_routes
    from msingi_app_backend.configs.database_config import Base, engine

else:
    from .msingi_app_backend.configs.database_config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})

# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(project_routes, prefix="/v1")
app.include_router(project_routes, prefix="/v2")


get = app.get

@get("/")
async def homepage():
    """
    This is the api's home page.
    It currently redirects to the swagger docs.
    """
    return RedirectResponse('/redoc')

# Server should not run when called by pytest
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
