import fitz
from io import BytesIO
import json
import re


def get_text(file: BytesIO) -> str:
    """
    file: BytesIO object of the pdf file
    return: text extracted from the pdf file
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    # extract blocks of type text from doc

    blocks = [
        re.sub(r"\s+", " ", " ".join([span["text"]
               for line in block["lines"] for span in line["spans"]]))
        for page in doc
        for block in json.loads(page.get_text("json")).get("blocks", [])
        if block["type"] == 0
    ]

    text = "\n".join(blocks).strip()
    return text


def read_file(path: str) -> str:
    with open(path, "rb") as f:
        return get_text(BytesIO(f.read()))
