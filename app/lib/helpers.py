import os.path
from markdown import markdown

def mdtohtml(filename):
    """
    open markdown files and return json object
    in the form
    data = {'text': html}
    """
    filepath = os.path.join("app/md/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown(text)
    data = {
        "text": html
    }
    return data
