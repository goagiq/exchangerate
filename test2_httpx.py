import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Get the access key from the environment variables
ACCESS_KEY = os.getenv('ACCESS_KEY')

# Initialize the FastMCP server
mcp = FastMCP("Exchange Rate")

# Define the ExchangeRate API URI
API_URI = "https://api.exchangerate.host/convert"

@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Convert currency using the ExchangeRate API.

    Args:
        amount (float): The amount to convert.
        from_currency (str): The currency to convert from.
        to_currency (str): The currency to convert to.

    Returns:
        dict: The conversion result.
    """
    params = {
        'access_key': ACCESS_KEY,
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }
    response = httpx.get(API_URI, params=params)
    return response.json()

# Example usage of the convert_currency function
if __name__ == "__main__":
    # Example parameters
    mcp.run()