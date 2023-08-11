import pytest
from app.services import resume_service
from app.utils import pdfparser
import json


def test_load_env():
    from app.utils import load_env
    import os
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    assert OPENAI_API_KEY is not None, "OpenAI API key not found"


@pytest.mark.asyncio
async def test_resume_parsing():
    test_pdf_path = "tests/resources/resume1.pdf"
    expected_out_path = "tests/resources/output1.json"
    text = pdfparser.read_file(test_pdf_path)
    # Call the actual `resume_service` function with test pdf
    output_data = await resume_service.getResumeDetails(text)
    with open(expected_out_path) as f:
        expected_result = json.load(f)
    assert output_data is not None, "No response returned"

    # Assert that your actual output and expected output are same
    assert output_data.model_dump() == expected_result
