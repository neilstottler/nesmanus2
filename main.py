#let's try stitching with python
from jinja2 import Template
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn

app = FastAPI(
    title="my api",
    version="0.0.1",
    openapi_tags=[],
    docs_url="/api/docs/swagger",
    redoc_url="/api/docs/redoc",
    openapi_url="/api/docs/openapi.json",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

#if 404
@app.exception_handler(StarletteHTTPException)
async def error404(request, exc):
    if exc.status_code == 404:
        templates = Jinja2Templates(directory="views")

        return templates.TemplateResponse(
            "404.html",
            {"request": request, "title": "404 Not Found"},
            status_code=404
        )


@app.get("/")
async def root(request: Request):
    templates = Jinja2Templates(directory="views")
    
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "KitchenSink"}
    )

@app.get("/test")
async def root(request: Request):
    templates = Jinja2Templates(directory="views")
    
    return templates.TemplateResponse(
        "test.html", 
        {"request": request, "title": "KitchenSink"}
    )
#if __name__ == "__main__":
#    uvicorn.run(app, host="localhost", port="80")