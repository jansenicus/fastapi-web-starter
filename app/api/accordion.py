from . import * 


@api.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    tag = "flower"
    result = "Type a number"
    return html.TemplateResponse('accordion.html', context={'request': request, 'result': result, 'tag': tag})


@api.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):

    return html.TemplateResponse('accordion.html', context={'request': request, 'tag': tag})