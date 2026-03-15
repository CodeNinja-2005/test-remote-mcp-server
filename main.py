import json

from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

@mcp.resource("data://config")
def get_config() -> str:
    """Provides application configuration as JSON."""
    config = {
        "theme": "dark",
        "version": "1.2.0",
        "features": ["tools", "resources"],
        "tools": ["add", "multiply"],
    }
    return json.dumps(config, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
