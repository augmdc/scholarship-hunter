from crewai_tools import PDFSearchTool
from langchain.tools import tool
from PyPDF2 import PdfReader

@tool
def pdf_tool(path: str) -> str:
    """
    Fetches and preprocesses content from a PDF.
    Returns the text of the PDF.
    """
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

# TO-DO: Create a PDF scraper that finds hyperlinks in a PDF file
@tool
def hyperlink_extractor():
    """
    Takes in a pdf file, and extracts out hyperlinks with the piece of text that the URL was linked to
    """
    return ""