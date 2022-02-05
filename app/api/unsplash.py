from . import *
from os import getenv
from dotenv import load_dotenv
load_dotenv()

@api.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    return html.TemplateResponse("unsplash.html", {"request": request})