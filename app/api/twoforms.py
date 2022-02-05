from . import * 
from os import getenv


@api.get("/twoforms", response_class=HTMLResponse)
def form_get(request: Request):
    result = "Type a number"
    return html.TemplateResponse('twoforms.html', context={'request': request, 'result': result})


@api.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 2
    return html.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})


@api.post("/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: int = Form(...)):
    result = number + 100
    return html.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})

