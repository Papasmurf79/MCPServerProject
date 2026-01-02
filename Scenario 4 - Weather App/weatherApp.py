# MCP Inspector Command: npx @modelcontextprotocol/inspector weatherApp.py

import requests  # lets us fetch live data from APIs.
import os # used to access environment variables like port numbers.
import sys # allows the script to exit gracefully in case of errors.
import logging # records what your server is doing.
from mcp.server.fastmcp import FastMCP

# Set up logging configuration
name = "Weather App MCP"
logging.basicConfig(level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers = [logging.StreamHandler()]
)
logger = logging.getLogger(name)

port = int(os.environ.get('PORT', 8004)) # Default to 8004 if PORT not set
mcp = FastMCP(name=name, logger=logger, port=port)

@mcp.tool()
def get_current_weather(City: str) -> str:
    """Returns the weather for a given city."""
    logger.info(f"Get Current Weather for city: {City}")
    
    try:
        endpoint = "http://wttr.in"
        response = requests.get(f"{endpoint} / {City}", timeout=10)
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        logger.error(f"Error retriving weather data: {str(e)}")       
        return f"Error retriving weather data: {str(e)}"

# Run the server
if __name__ == "__main__":
    logger.info(f"Starting MCP server on port {port}...")
    try:
        mcp.run(transport="sse", host="localhost", port="8004")  # Start the MCP server with HTTP transport
    except Exception as e:  
        logger.error(f"Failed to start MCP server: {str(e)}")
        sys.exit(1)
    finally:
        logger.info("server has stopped.")    