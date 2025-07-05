"""
This module sets up a MCP (Model Context Protocol) server for integrating GroundX tools with the FastMCP framework.

Environment variable loading priority:
- If GROUNDX_API_KEY is already set in the environment (e.g., via claude_desktop_config.json), it will be used.
- Otherwise, the value from the .env file (if present) will be loaded via dotenv.

Key functionalities:
- Dynamically loads tool modules from the 'groundx_mcp_tools' directory.
- Wraps each tool function to automatically provide the API key.
- Registers each tool with the FastMCP server under its module name.
- Runs the MCP server using stdio transport.
"""

from mcp.server.fastmcp import FastMCP
import os
import sys
from dotenv import load_dotenv
from functools import partial
import importlib
import pkgutil

# Loading environment variables from the environment prescribed in the config file
groundx_api_key = os.getenv("GROUNDX_API_KEY")
if not groundx_api_key:
    # If GROUNDX_API_KEY could not be found, load it from the .env file
    print("GROUNDX_API_KEY not set in config file, loading from .env", file=sys.stderr)
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
    groundx_api_key = os.getenv("GROUNDX_API_KEY")

def make_tool(func):
    """
    Wraps a tool function to inject the GroundX API key as the first argument.
    Also cleans up the docstring for user-facing documentation.
    """
    tool = partial(func, groundx_api_key)
    tool.__name__ = func.__name__
    tool.__doc__ = func.__doc__
    if tool.__doc__:
        # Remove the first argument line mentioning the groundx API key
        lines = tool.__doc__.splitlines()
        filtered_lines = [line for line in lines if not line.strip().startswith('groundx_api_key')]
        tool.__doc__ = '\n'.join(filtered_lines).strip()
    return tool

def get_groundx_tools():
    """
    Dynamically discovers and loads all modules in the 'groundx_mcp_tools' package.
    Returns a list of (name, wrapped function) tuples for registration with the MCP server.
    """
    tools = []
    package = 'groundx_mcp_tools'
    package_path = os.path.join(os.path.dirname(__file__), package)
    for _, modname, _ in pkgutil.iter_modules([package_path]):
        module = importlib.import_module(f"{package}.{modname}")
        func = getattr(module, modname)
        tools.append((modname, make_tool(func)))
    return tools

# Creates the FastMCP server instance and registers the tools from the groundx_mcp_tools package
mcp = FastMCP("Groundx-RAG-MCP-Server")
for name, func in get_groundx_tools():
    mcp.tool(name=name)(func)

def main():
    """
    Runs the MCP server with stdio transport.
    """
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
