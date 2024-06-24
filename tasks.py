from crewai import Task
from crewai_tools import ScrapeWebsiteTool, PDFSearchTool, FileReadTool
from agents import document_reader, context_analyzer, deadline_checker
from tools import pdf_tool

# Task 1: Extract Scholarship Information
extract_scholarship_information = Task(
    description=(
        "Extract scholarship details, links and deadlines from the document at the following path: {file_path}. "
        "Ensure all relevant information is captured accurately."
    ),
    expected_output="A list of scholarships with their details and links in JSON format.",
    tools=[pdf_tool],
    output_file='tmp1.json',
    agent=document_reader
)

# Task 2: Analyze Eligibility
analyze_eligibility = Task(
    description=(
        "Analyze the user's context and filter scholarships based on eligibility criteria. "
        "Context: {user_context}"
    ),
    expected_output="A list of scholarships the user is actually eligible for in JSON.",
    output_file='tmp2.json',
    agent=context_analyzer
)

# Task 3: Check Deadlines
check_deadlines = Task(
    description=(
        "Check the deadlines of the scholarships and filter out those that have passed. "
        "Ensure to verify the deadlines from the provided links AND the document."
    ),
    expected_output="A final list of scholarships that the user can still apply for, with unexpired deadlines in JSON.",
    tools=[ScrapeWebsiteTool()],
    output_file='final.json',
    agent=deadline_checker
)

# Export tasks
tasks = [extract_scholarship_information, analyze_eligibility, check_deadlines]


