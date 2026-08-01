from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


load_dotenv()

llm= ChatGoogleGenerativeAI(model="gemma-4-31b-it")

response= llm.invoke("How many moons does Jupiter have?")
print(response.text)

# Implementing Temperature
prompt = "Write a single name for new jewelry company. Out onlyput the name, that's all."

llm = ChatGroq(
    model="llama-3.3-70b-versatile", temperature=1
)

response = llm.invoke(prompt)
print(response.content)