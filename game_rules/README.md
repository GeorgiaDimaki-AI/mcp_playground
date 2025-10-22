# Game Rules Directory

Place your game rule PDF files in this directory.

## Naming Convention

Use descriptive names with lowercase letters, hyphens, or underscores:

**Good examples**:
- `chess.pdf`
- `monopoly.pdf`
- `settlers-of-catan.pdf`
- `dungeons-and-dragons.pdf`
- `ticket-to-ride.pdf`

**Avoid**:
- Spaces in filenames
- Special characters
- UPPERCASE names

## File Format

- Only PDF files are supported
- PDFs must be text-based (not scanned images without OCR)
- PDFs should be the official rulebooks for games

## Usage

Once you add PDF files here, they will automatically be available through the MCP server. You can:

1. List all games using the `list_games` tool
2. Search within game rules using the `search_game_rules` tool
3. Access full rulebooks as resources via `game://<game-name>`

## Example

If you add a file named `chess.pdf`, you can:

- Search it: `search_game_rules(game="chess", query="castling")`
- Read it as a resource: `game://chess`
- Get info: `get_game_summary(game="chess")`
