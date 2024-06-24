# TO-DO: Create a PDF scraper that handles PDF files well
from crewai_tools import PDFSearchTool

pdf_tool = PDFSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="phi3",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="ollama", # or openai, ollama, ...
            config=dict(
                model="all-minilm",
                # task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)