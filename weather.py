from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather") 

@mcp.tool()  # mcp.tool() operate here as a Decorator to register the function as a tool in FastMCP like and SDK
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.

    Args:
        location (str): The location to get the weather for can be city, country, sate, etc.
    """
    return "The weather is hot and dry"

if __name__ == "__main__":
    mcp.run()  # Run the FastMCP server