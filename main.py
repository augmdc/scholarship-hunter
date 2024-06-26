from crewai import Crew, Process
from tasks import tasks
from agents import document_reader

context = """
I am a Graduate level Engineering student, pursuing a Master's in Applied Science (Engineering Science).
"""

file_path = "/Users/augmdc/Desktop/ExternalAwards.pdf"

# Crew 1: Get relevant scholarships
search_crew = Crew(
    agents=[document_reader],
    tasks=tasks,
    process=Process.sequential
)

result = search_crew.kickoff(inputs={
    'user_context': context,
    'file_path': file_path,
})

print(result)

# Crew 2: Write out essay based on criteria
# TO-DO