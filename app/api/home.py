from . import * 
from ..lib.helpers import mdtohtml

@api.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = mdtohtml("home.md")
    return html.TemplateResponse("page.html", {"request": request, "data": data})