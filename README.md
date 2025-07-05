# RAG GroundX MCP Server

An MCP (Model Context Protocol) server for interacting with the GroundX API from eyelevel.ai, featuring a local proxy to connect to the remote Google Drive MCP Server URL of your choice (for example, Zapier). This integration enables seamless integration of GroundX capabilities into your GitHub Copilot and Claude Desktop workflows to perform advanced parsing and semantic search on your Google Drive or local documents.

## 🌟 Key Features

- **MCP Server for GroundX API** with stdio transport
- **Google Drive Integration** through MCP Proxy
- **Dual Document Management**:
  - Upload local files directly to GroundX
  - Or sync Google Drive documents with GroundX
- **Advanced Semantic Search** across all your documents
- **Seamless Integration** with:
  - GitHub Copilot
  - Claude Desktop

## 🚀 Quick Start

### Prerequisites

- Windows with WSL 2 installed (Ubuntu 22.04 recommended)
- [Install uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) if you haven't already- Python 3.11 or higher
- A [GroundX API key](https://dashboard.eyelevel.ai/home) (free tier available)
- (Optional) A Google Drive MCP Server URL - for example using [Zapier](https://zapier.com/app/home) (free tier available) - and a Google account dedicated to this Google Drive integration.

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Geoffrey-42/rag-groundx-mcp-server.git
   cd rag-groundx-mcp-server
   ```

2. **Set up the virtual environment**:
   ```bash
   # Create and activate virtual environment
   uv venv
   
   # Activate the virtual environment
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   uv pip install -r requirements.txt
   ```

4. (Optional) **Configure your environment within a .env file**:
   - Create a `.env` file in the root directory:
     ```bash
     touch .env
     ```
   - Edit the `.env` file and add your credentials:
     ```
     # Required: Get your API key from https://dashboard.eyelevel.ai/home
     GROUNDX_API_KEY=your_groundx_api_key_here
     
     # Optional: Only needed for Google Drive integration
     # GOOGLE_DRIVE_SERVER_URL=your_google_drive_mcp_server_url
     ```
   - Note: Can be skipped if you configure the environment within the claude_desktop_config.json file (see below).

## 🔌 Claude Desktop Configuration

To use this server with Claude Desktop and GitHub Copilot:

1. **Configure the `claude_desktop_config.json` file**:
   - Location: `%APPDATA%\Claude\claude_desktop_config.json` (Windows)
   - Add the following MCP servers to the configuration and fill the placeholders with your values to configure the servers:
   
   ```json
   {
     "mcpServers": {
       "Groundx_RAG_MCP_Server": {
         "command": "wsl",
         "args": [
           "-d", "Ubuntu-22.04",
           "-e", "bash", "-c",
           "export GROUNDX_API_KEY=<your_groundx_api_key> && export PATH=$HOME/.local/bin:$PATH && cd /home/<your-name>/<project-folder>/rag-groundx-mcp-server/src && uv run Groundx_RAG_MCP_Server.py"
         ],
         "env": {
           "GROUNDX_API_KEY": "<your_groundx_api_key>"
         }
       },
       "GoogleDriveProxyServer": {
         "command": "wsl",
         "args": [
           "-d", "Ubuntu-22.04",
           "-e", "bash", "-c",
           "export GOOGLE_DRIVE_SERVER_URL=<your_google_drive_mcp_server_url> && export PATH=$HOME/.local/bin:$PATH && cd /home/<your-name>/<project-folder>/rag-groundx-mcp-server/src && uv run Google_Drive_Proxy_Server.py"
         ],
         "env": {
           "GOOGLE_DRIVE_SERVER_URL": "<your_google_drive_mcp_server_url>"
         }
       }
     }
   }
   ```

Note 1: You can either use the environment variables or the command line arguments to pass the API key and Google Drive MCP Server URL. In theory, you can use the environment variables parameters "env" for both servers, but it is recommended to use the command line arguments "args" to avoid issues in the WSL environment. Hence here, both methods are shown. 

Note 2: You can also use the .env file to pass the API key and Google Drive MCP Server URL to the servers. Write GOOGLE_DRIVE_SERVER_URL = <your_google_drive_mcp_server_url> and GROUNDX_API_KEY = <your_groundx_api_key> in the .env file.

Note 3: You must also specify the path to the root directory of the project (for example, /home/<your-name>/<project-folder>/rag-groundx-mcp-server/src) in the command line arguments "args".

Note 4: You may also use fastmcp.cli.claude to configure the MCP servers in Claude Desktop. See https://gofastmcp.com/python-sdk/fastmcp-cli-claude#fastmcp-cli-claude for more information.


2. **Restart Claude Desktop and VS Code** (File->Quit) to apply changes

Once configured for Claude Desktop, the MCP tools will also be available in VS Code through GitHub Copilot.
After restarting Claude Desktop and VS Code, the VS Code agent or Claude Desktop will automatically detect and use these tools when relevant.
Don't forget to enable Agent mode in VS Code and to enable the MCP tools in Claude Desktop.

## 🤖 GitHub Copilot Integration

To use this server with GitHub Copilot:

1. Enable Agent mode in VS Code
2. MCP tools will be automatically detected
3. Interact naturally - the agent will use the appropriate tools as needed

## 🚀 Quick Start with Claude Desktop

1. Ensure MCP servers are running via Claude Desktop configuration
2. Verify the presence of your MCP tools by clicking on the tools logo below the chat input field of Claude Desktop.
3. Interact naturally - the agent will use the appropriate tools as needed.
4. You may ask Claude to search for documents in your Google Drive.
5. You may ask Claude to upload documents from your Google Drive to GroundX.
6. You may ask Claude to answer a query based on your GroundX documents using the Retrieval tool.

## 🚀 Quick Start with GitHub Copilot

1. Ensure MCP servers are running via Claude Desktop configuration.
2. Open VS Code and enable Agent mode in GitHub Copilot.
3. Verify the presence of your MCP tools by clicking on the tools logo below the chat input field of GitHub Copilot.
4. Interact naturally - the agent will use the appropriate tools as needed.
5. For uploading local files to groundx: Open this project folder under WSL in VS Code. The agent will then have access to it any documents you may copy to within this folder.
6. You may ask the agent to search for documents in your Google Drive.
7. You may ask the agent to upload documents from your Google Drive to GroundX.
8. You may ask the agent to answer a query based on your GroundX documents using the Retrieval tool.

### Example Interaction

When working in VS Code with GitHub Copilot enabled, you can simply describe what you want to do in natural language, and the agent will automatically use the appropriate MCP tools. For example:

1. **General information**: "List my groundx buckets and my google drive documents"
2. **Upload local file to groundx**: "Upload the file path/to/document.pdf from my local machine to my groundx bucket with id <bucket_id>"
3. **Search for documents**: "Find <article_name>.pdf in my <folder_name> folder in google drive and make it ready to be ingested in my groundx bucket with id <bucket_id>."
4. **Upload documents**: "Add this document from my google drive to my groundx bucket with id <bucket_id>"
5. **Retrieve knowledge**: Ask the agent to answer a query after it has retrieved information from your groundx documents.

The agent will handle all the tool invocations and API calls automatically based on your natural language requests.

## 📚 Available Tools

### Main Tools

- `Retrieval_from_Groundx`: Performs semantic search across your documents
- `upload_local_file_to_Groundx`: Uploads a local file to GroundX
- `upload_remote_file_to_Groundx`: Uploads a file from a public URL to GroundX
- `crawl_website_to_Groundx`: Crawls and uploads a website to GroundX
- `google_drive_retrieve_files_from_google_drive`: Retrieves details of a specific document from Google Drive. Available only if you have configured a Google Drive MCP Server URL (for example, with Zapier), and copied it in the .env file as GOOGLE_DRIVE_SERVER_URL or in your claude_desktop_config.json file.
- Many others

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For questions or issues, please open an issue in the repository.
