# Quick Start Guide

Get started with the Game Rules MCP Server in 3 steps:

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Add Your Game Rule PDFs

Place PDF files in the `game_rules/` directory:

```bash
cp /path/to/your/chess-rules.pdf game_rules/chess.pdf
cp /path/to/your/monopoly-rules.pdf game_rules/monopoly.pdf
```

**Important**:
- Only text-based PDFs work (not scanned images)
- Use lowercase names with hyphens or underscores
- Don't include spaces in filenames

## Step 3: Configure Claude Desktop (or your MCP client)

Edit your Claude Desktop config file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

Add this configuration (update the path to match your installation):

```json
{
  "mcpServers": {
    "game-rules": {
      "command": "python",
      "args": ["/full/path/to/mcp_playground/claude_code/game-rules-pdf-server/game_rules_server.py"]
    }
  }
}
```

## Step 4: Restart Claude Desktop

Restart Claude Desktop to load the MCP server.

## Testing It Works

Try asking Claude:

- "What game rulebooks do you have available?"
- "Search the chess rules for 'castling'"
- "Give me a summary of the Monopoly rules"

## Getting Game Rule PDFs

You can find game rule PDFs from:

1. **Publisher Websites**: Many game publishers offer official rulebooks as free PDFs
2. **BoardGameGeek**: Community-uploaded rulebooks (check copyright)
3. **Your Own Games**: Scan or download the rules for games you own

### Example Sources:

- **Chess**: FIDE Laws of Chess (fide.com)
- **Monopoly**: Hasbro official rules
- **Scrabble**: Official Scrabble rules
- **Catan**: Catan.com official rules
- **Magic: The Gathering**: Wizards of the Coast comprehensive rules

## Troubleshooting

**"No game rulebooks found"**
- Make sure PDF files are in the `game_rules/` directory
- Check that files have `.pdf` extension

**"Game rulebook not found: xyz"**
- Use the exact filename without `.pdf` extension
- Example: For `chess.pdf`, use `game="chess"`

**Search returns no results**
- Try simpler search terms
- Check spelling
- Some PDFs may have formatting that affects text extraction

## Need Help?

Check the full [README.md](README.md) for more detailed documentation.
