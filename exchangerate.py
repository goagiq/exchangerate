import os
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Get the access key from the environment variables
ACCESS_KEY = os.getenv('ACCESS_KEY')

# Define the URI for the API
API_URI = "https://api.exchangerate.host/convert"

# Initialize the FastMCP server
mcp = FastMCP("Exchange Rate")

# Function to get exchange rate
@mcp.tool()
def get_exchange_rate(from_currency, to_currency, amount):
    params = {
        'access_key': ACCESS_KEY,
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }
    response = requests.get(API_URI, params=params)
    data = response.json()
    if response.status_code == 200:
        return data['result']
    else:
        return data['error']['info']

# Create the Gradio interface
def gradio_interface(from_currency, to_currency, amount):
    try:
        result = get_exchange_rate(from_currency, to_currency, amount)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Launch the Gradio interface
if __name__ == "__main__":
    iface = gr.Interface(
        fn=gradio_interface,
        inputs=[
            gr.Textbox(lines=1, placeholder="From Currency (e.g., USD)"),
            gr.Textbox(lines=1, placeholder="To Currency (e.g., EUR)"),
            gr.Number(value=1, label="Amount")
        ],
        outputs=gr.Textbox(label="Result")
    )
    iface.launch()