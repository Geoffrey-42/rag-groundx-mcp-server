from fastmcp import FastMCP
import asyncio
from dotenv import load_dotenv
import os
import sys

# Loading environment variables from the environment prescribed in the config file
google_drive_server_url = os.getenv("GOOGLE_DRIVE_SERVER_URL")
if not google_drive_server_url:
    # If GOOGLE_DRIVE_SERVER_URL could not be found, load it from the .env file
    print("GOOGLE_DRIVE_SERVER_URL not set in config file, loading from .env", file=sys.stderr)
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
    google_drive_server_url = os.getenv("GOOGLE_DRIVE_SERVER_URL")
print(google_drive_server_url, file=sys.stderr)

proxy_server = FastMCP.as_proxy(
    google_drive_server_url,
    name="GoogleDriveProxyServer"
)

asyncio.run(proxy_server.run_async(transport="stdio"))