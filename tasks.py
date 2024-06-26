from crewai import Task
from crewai_tools import ScrapeWebsiteTool
from agents import document_reader, context_analyzer

# Task 1: Extract Scholarship Information
extract_scholarship_information = Task(
    description=(
        """
        Here’s an improved version of your task description for better clarity and structure:

---

### Task Description

**Step 1: Extract Scholarship Details**

1. Extract scholarship details, links, and deadlines from the document located at the following path: `{file_path}`.
2. Ensure all relevant information is captured accurately.
```

---

By following these steps and maintaining the specified output format, you ensure that the task is clear and the resulting data is consistent and accurate.
        """
    ),
    expected_output="A list of scholarships with their details and links.",
    output_file='Scholarships.txt',
    agent=document_reader
)

# Export tasks
tasks = [extract_scholarship_information]

prompt_experiment = """
**Step 2: Filter Scholarships Based on User Context**

1. Analyze the user's context and filter scholarships based on eligibility criteria using the following context:
   - Context: `{user_context}`

**Output Format**

The output should be formatted exactly as follows:

```
Scholarship Name 1
Application Deadline: June 25th, 2024
URL: http://example.com
Amount: $5000

Scholarship Name 2
Application Deadline: June 25th, 2024
URL: None
Amount: $5000
"""
