from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langserve import add_routes
from fastapi import FastAPI

llm = OpenAI(temperature=0)
prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
chain = LLMChain(llm=llm, prompt=prompt)

app = FastAPI()
add_routes(app, chain, path="/name-generator")
