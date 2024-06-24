from langchain_community.llms import Ollama
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, PDFSearchTool, FileReadTool
from tools import pdf_tool

llm = Ollama(model="phi3")

document_reader = Agent(
    role='Document Reader',
    goal='Extract scholarship details, links, and deadlines from the provided document.',
    backstory="",
    verbose=True,
    memory=True,
    tools=[pdf_tool],
    llm=llm
)

context_analyzer = Agent(
    role='Context Analyzer',
    goal="""
        Based on the user's context, filter scholarships that they can apply for.
        """,
    backstory="",
    verbose=True,
    memory=True,
    llm=llm
)

deadline_checker = Agent(
    role='Deadline Checker',
    goal='Check the deadlines of the scholarships and filter out those that have passed.',
    backstory="",
    verbose=True,
    memory=True,
    tools=[ScrapeWebsiteTool()],
    llm=llm
)