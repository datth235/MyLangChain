from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Model chạy local bằng Ollama
model = ChatOllama(
    model="qwen3:4b"
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Chain
chain = prompt | model

# Gọi model
response = chain.invoke({
    "topic": "machine learning"
})

print(response.content)