# Project Prompt

This file contains the original prompt used to generate this project. It's included to enable fair comparisons across different AI coding tools and to document the project's requirements.

## Original Request

**AI Tool Used**: Claude Code
**Date**: 2025-10-22
**Session**: claude/game-rules-pdf-server-011CUNGKVBBYTRhBW2nwrkji

## The Prompt

### Initial Request

```
I would like to make an mcp server for game rules. I have a set of pdfs
for games and I want my user to be able to ask things about the games
and get responses based on the pdf materials.
```

### Structured Version

**Objective**: Create an MCP (Model Context Protocol) server for querying game rules from PDF files.

**Requirements**:
1. **PDF Support**: The server should work with PDF files containing game rulebooks
2. **Storage**: Users should be able to store multiple game rule PDFs
3. **Querying**: Users should be able to ask questions about game rules
4. **Responses**: The server should provide answers based on the PDF content

**Expected Functionality**:
- Read and parse PDF files
- Extract text content from game rulebooks
- Allow users to search/query the rules
- Return relevant information from the PDFs
- Support multiple game rulebooks

**User Story**:
As a board game player, I want to quickly look up specific rules from my game
rulebooks without manually searching through PDF files, so that I can resolve
questions during gameplay.

## Implementation Notes

The resulting implementation (by Claude Code) included:

### Core Features
- **Resources**: Expose each PDF as an MCP resource (`game://<game-name>`)
- **Tools**:
  - `list_games` - List all available rulebooks
  - `search_game_rules` - Search within a specific game's rules
  - `get_game_summary` - Get metadata and preview of a rulebook

### Technical Stack
- **Language**: Python 3.10+
- **Libraries**:
  - `mcp>=1.0.0` - MCP SDK
  - `PyPDF2>=3.0.0` - PDF parsing
  - `pydantic>=2.0.0` - Data validation

### Project Structure
- MCP server implementation (`game_rules_server.py`)
- PDF storage directory (`game_rules/`)
- Comprehensive documentation (README, QUICK_START)
- Example configuration files
- Python packaging setup

## Using This Prompt

### For Comparison Testing

To test how different AI coding tools approach this task:

1. **Copy the structured prompt** above
2. **Provide it to your AI coding tool** (Cursor, Copilot, etc.)
3. **Let it generate the implementation**
4. **Compare the results** with this implementation

### Comparison Criteria

When comparing implementations, consider:

- **Completeness**: Does it include all required functionality?
- **Code Quality**: Is the code well-structured and documented?
- **Error Handling**: How robust is the implementation?
- **Documentation**: Quality of README, comments, and examples
- **User Experience**: How easy is it to set up and use?
- **Additional Features**: What extra capabilities were added?

### Fair Comparison Guidelines

For fair comparison across AI tools:
- Use the same base prompt
- Provide similar context (mention MCP if needed)
- Allow the AI to make design decisions
- Don't over-specify implementation details
- Let each tool showcase its strengths

## Variations to Try

You can modify this prompt to test different capabilities:

### More Specific
```
Create an MCP server that:
- Reads game rule PDFs from a directory
- Provides full-text search across all pages
- Returns context around search matches
- Exposes PDFs as MCP resources
- Includes error handling and logging
```

### More Open-Ended
```
Build a tool that helps board game players quickly find rules
from their PDF rulebooks using an AI assistant.
```

### Different Focus
```
I need an MCP server for game rules. Focus on making the search
results really useful with good context and examples.
```

## License

This prompt and documentation are part of the MCP Playground project (MIT License).

---

**Note**: This prompt is provided as-is for educational and comparison purposes.
Feel free to adapt it for your own experiments with different AI coding tools.
