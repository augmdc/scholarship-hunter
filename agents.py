from langchain_community.llms import Ollama
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
from tools import pdf_tool

llm = Ollama(model="phi3")

document_reader = Agent(
    role='Document Reader',
    goal="""
        Extract the following details from the provided document: scholarship name, link, application deadline, eligibility criteria, and amount.
        The output should be in the following format:

        Scholarship Name
        Application Deadline (as Numbers)
        Eligibility Criteria:
            - Criteria1
            - Criteria2
            - Criteria3
        Amount

        """,
    backstory="",
    verbose=True,
    memory=True,
    tools=[pdf_tool],
    llm=llm
)

context_analyzer = Agent(
    role='Context Analyzer',
    goal="""
        Based on context given to you from a student, filter scholarships that they can apply for.
        Be sure to only use criteria that you can extract from the user context.
        Take it step by step.

        If if it is not obvious that the user should apply to this scholarship, visit the link associated with the scholarship to see if it is the right fit.
        """,
    backstory="You are a helpful AI assistant whose only job is to take a user's context and to find which scholarships would apply to them.",
    verbose=True,
    memory=True,
    tools=[ScrapeWebsiteTool()],
    llm=llm
)

deadline_checker = Agent(
    role='Deadline Checker',
    goal="""
        You are an assistant. From the provided list of scholarships in JSON format,
        check the deadlines of the scholarships and filter out those that have passed.
        Return the remaining scholarships in JSON format. Take it step by step.
        """,
    backstory="You are a helpful AI assistant.",
    verbose=True,
    memory=True,
    tools=[ScrapeWebsiteTool()],
    llm=llm
)