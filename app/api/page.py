from . import *
from ..lib.helpers import mdtohtml

@api.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = mdtohtml(page_name+".md")
    return html.TemplateResponse("page.html", {"request": request, "data": data})