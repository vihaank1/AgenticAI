from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent

load_dotenv

PRODUCTS = {
    "wireless headphones": {"price": 79.99, "description": "Over-ear Bluetooth, 30-hr battery, active noise cancellation."},
    "smart watch":         {"price": 199.99, "description": "Tracks heart rate and sleep. 5-day battery, water-resistant."},
    "mechanical keyboard": {"price": 129.00, "description": "Tenkeyless, Cherry MX Brown switches, per-key RGB."},
    "laptop stand":        {"price": 34.99, "description": "Adjustable aluminium, fits 11-17 in laptops, folds flat."},
}

@tool
def get_product(name: str) -> str:
    """Look up a product by name and return its price, rating stock, & description."""
    p = PRODUCTS.get(name.lower())
    if not p:
        return f"Product not found. Available: {', '.join(PRODUCTS)}"
    return str(p)

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

agent = create_agent(
     llm,
     tools=[get_product],
     system_prompt="You are a helpful product assistant for an online tech store."
)

def ask(question: str):
    result=agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)

ask("what is the price of wireless headphones.")


REVIEWS = {
    "wireless headphones": {"reviews": 1262, "rating": 4.6},
    "smart watch":         {"reviews": 340, "rating": 3.9},
    "mechanical keyboard": {"reviews": 67,  "rating": 4.8},
    "Laptop stand":        {"reviews": 781, "rating": 4.5},
}

@tool
def get_review(name: str) -> str:
    """Look up a product review by a product name. Return the product name, num of reviews & rating."""
    r = REVIEWS.get(name.lower())
    if not r:
        return f"Review not available for this product"
    return str(r)


from langgraph.checkpoint.memory import InMemorySaver

agent2 = create_agent(
     llm,
     tools=[get_product, get_review],
     system_prompt="You are a helpful product assistant for an online tech store."
)

def ask2(question: str):
    config = {"configurable": {"thread_id": "user-alice-session-1"}}
    result=agent2.invoke(
        {"messages": [{"role": "user", "content": question}]})
    print(result["messages"][-1].content)

ask2("What makes fancy watches so attractive?")



