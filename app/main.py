from . import *
from app.api import home, page, twoforms, unsplash, accordion

API = FastAPI()
API.mount("/static", StaticFiles(directory="res"), name="static")

API.include_router(home.api)
API.include_router(page.api)
API.include_router(unsplash.api)
API.include_router(twoforms.api)
API.include_router(accordion.api)