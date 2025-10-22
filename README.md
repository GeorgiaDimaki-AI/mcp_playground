# Game Rules MCP Server

A Model Context Protocol (MCP) server that provides access to game rule PDFs, enabling AI assistants to help users understand and query board game rules.

## Features

- **Resources**: Access complete game rulebooks as resources
- **Search**: Search for specific rules or keywords within game PDFs
- **List Games**: View all available game rulebooks
- **Summaries**: Get quick summaries and metadata about game rules

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd mcp_playground
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using pip with pyproject.toml:
```bash
pip install -e .
```

## Adding Game Rules

Place your game rule PDF files in the `game_rules/` directory. The files should be named descriptively, using lowercase with hyphens or underscores:

```
game_rules/
├── chess.pdf
├── monopoly.pdf
├── settlers-of-catan.pdf
└── dungeons-and-dragons.pdf
```

## Usage

### Running the Server

The server uses stdio for communication:

```bash
python game_rules_server.py
```

### Configuring with Claude Desktop

Add this server to your Claude Desktop configuration file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "game-rules": {
      "command": "python",
      "args": ["/path/to/mcp_playground/game_rules_server.py"]
    }
  }
}
```

Or if installed with pip:
```json
{
  "mcpServers": {
    "game-rules": {
      "command": "game-rules-server"
    }
  }
}
```

### Configuring with Other MCP Clients

Use the standard MCP stdio protocol to connect to the server:

```python
# Example Python client
import asyncio
from mcp.client import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["game_rules_server.py"]
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        # Use the session...
```

## Available Tools

### 1. `list_games`
Lists all available game rulebooks in the system.

**Parameters**: None

**Example**:
```
list_games()
```

### 2. `search_game_rules`
Search for specific text or rules within a game's rulebook.

**Parameters**:
- `game` (required): Name of the game (without .pdf extension)
- `query` (required): Text to search for in the rules
- `case_sensitive` (optional): Whether search should be case-sensitive (default: false)

**Example**:
```
search_game_rules(game="chess", query="castling")
```

### 3. `get_game_summary`
Get a summary of a game's rules including page count and basic info.

**Parameters**:
- `game` (required): Name of the game (without .pdf extension)

**Example**:
```
get_game_summary(game="monopoly")
```

## Available Resources

Each PDF in the `game_rules/` directory is exposed as a resource with the URI format:

```
game://<game-name>
```

For example:
- `game://chess` - Complete Chess rules
- `game://monopoly` - Complete Monopoly rules

## Example Queries

Once configured with an AI assistant, you can ask questions like:

- "What are the rules for castling in chess?"
- "How do you win at Monopoly?"
- "Search the Catan rules for 'longest road'"
- "What games do you have available?"
- "Give me a summary of the Dungeons and Dragons rules"

## Development

### Project Structure

```
mcp_playground/
├── game_rules_server.py    # Main MCP server implementation
├── game_rules/             # Directory for PDF files
├── pyproject.toml          # Python project configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

### Dependencies

- `mcp>=1.0.0` - Model Context Protocol SDK
- `PyPDF2>=3.0.0` - PDF parsing and text extraction
- `pydantic>=2.0.0` - Data validation

## Troubleshooting

### PDFs Not Found
- Ensure PDF files are in the `game_rules/` directory
- Check that filenames use lowercase with hyphens or underscores
- When calling tools, use the filename without the .pdf extension

### Text Extraction Issues
- Some PDFs with complex formatting may not extract perfectly
- Scanned PDFs without OCR will not work (text-based PDFs only)
- Try re-exporting the PDF with text selection enabled

### Server Connection Issues
- Verify the path in your MCP client configuration is correct
- Ensure Python and dependencies are installed
- Check that the server starts without errors

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
