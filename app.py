from fastapi import FastAPI
from routers.user import user
from config.tags import tags_metadata 

app=FastAPI(
    title="here goes the title of the appi",
    description="here goes the description",
    version="version",
    #openapi_tags=[{"name":"users","description":"here goes the description of the tags"},{"name":"delite","description":"here goes the description of the tags"}]
    openapi_tags=tags_metadata
)

app.include_router(user)