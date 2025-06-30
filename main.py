from fastapi import FastAPI
from langserve import add_routes
from langchain_community.llms import Ollama

app = FastAPI(
    title="LangServe Agent",
    description="A LangChain server with Ollama integration"
)

# Configure Ollama to connect to your Ollama service in Kubernetes
# The service name 'ollama' will resolve to your Ollama pod
llm = Ollama(
    model="starcoder",
    base_url="http://ollama:11434"  # Use the Kubernetes service name
)

add_routes(app, llm, path="/ollama")

@app.get("/")
async def root():
    return {"message": "LangServe Agent is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}