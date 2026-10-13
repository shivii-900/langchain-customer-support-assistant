from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    project="project-7ae2949e-d62f-4ee4-8d9",
    location="global",
    vertexai=True,
    temperature=0,
    max_retries=2,
)