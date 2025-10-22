# Prompt: Game Rules PDF Server

**Type**: MCP Server
**Difficulty**: Intermediate
**Skills**: PDF parsing, MCP protocol, API design

## The Prompt

### Original Request

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

## Implementations

This prompt has been implemented by the following AI coding tools:

### ✅ Claude Code
- **Location**: [`claude_code/game-rules-pdf-server/`](../claude_code/game-rules-pdf-server/)
- **Date**: 2025-10-22
- **Language**: Python
- **Features Added**:
  - MCP Resources (expose PDFs as `game://<name>`)
  - Three tools: `list_games`, `search_game_rules`, `get_game_summary`
  - Context-aware search (shows surrounding lines)
  - Page-by-page parsing
  - Comprehensive documentation (README, QUICK_START)
  - Example configuration files
- **Libraries Used**: `mcp`, `PyPDF2`, `pydantic`
- **Notable Choices**:
  - Used PyPDF2 for PDF parsing
  - Async/await pattern throughout
  - Strong focus on documentation
  - Directory-based PDF storage (`game_rules/`)

### ⏳ Cursor
- **Status**: Not yet implemented
- Try this prompt with Cursor and add your implementation to `cursor/game-rules-pdf-server/`!

### ⏳ GitHub Copilot
- **Status**: Not yet implemented
- Try this prompt with Copilot and add your implementation to `copilot/game-rules-pdf-server/`!

### ⏳ Other Tools
- Try with Codeium, Tabnine, Replit AI, or any other AI coding assistant

## Usage Instructions

### For New Implementations

1. **Copy the structured prompt** above
2. **Start a new session** with your AI coding tool
3. **Paste the prompt** (you can use the original or structured version)
4. **Let the AI implement** the solution
5. **Save to the appropriate vendor folder**: `<vendor>/game-rules-pdf-server/`
6. **Update this file** to document your implementation

### Guidelines for Fair Comparison

To ensure fair comparison across tools:

- ✅ **DO** use the prompt as-is without heavy modification
- ✅ **DO** let the AI make its own design decisions
- ✅ **DO** allow the AI to choose libraries and frameworks
- ✅ **DO** let the AI determine project structure
- ❌ **DON'T** over-specify implementation details
- ❌ **DON'T** provide example code upfront
- ❌ **DON'T** force the AI to match another implementation

You can provide clarifications if the AI asks questions, but avoid steering it toward a specific solution.

## Comparison Criteria

When evaluating implementations, consider:

### Functionality (Core Requirements)
- ✅ Reads PDF files
- ✅ Parses and extracts text
- ✅ Supports multiple games/PDFs
- ✅ Provides querying/searching capability
- ✅ Follows MCP protocol

### Additional Features
- Advanced search (context, highlighting, scoring)
- Resource exposure (MCP resources)
- Multiple tools/endpoints
- Error handling and validation
- Configuration options

### Code Quality
- Project organization and structure
- Code readability
- Type hints and validation
- Error handling
- Testing

### Documentation
- README completeness
- Setup instructions
- Usage examples
- API documentation
- Troubleshooting guide

### Developer Experience
- Installation simplicity
- Configuration ease
- Dependencies count
- Example files provided
- Getting started time

### User Experience
- Search result quality
- Response formatting
- Error messages
- Performance
- Reliability

## Variations to Try

Want to test different aspects of AI coding tools? Try these variations:

### Minimal Prompt
```
Build an MCP server that lets me query game rule PDFs.
```

### Detailed Prompt
```
Create an MCP server that:
- Reads game rule PDFs from a configurable directory
- Provides full-text search with context around matches
- Returns relevant page numbers
- Exposes each PDF as an MCP resource
- Includes comprehensive error handling
- Has detailed documentation and examples
```

### Performance-Focused
```
I need a fast MCP server for querying large game rule PDFs.
Focus on performance and handling multiple concurrent requests.
```

### UX-Focused
```
Build an MCP server for game rules that prioritizes great search
results - make it easy to find exactly what players are looking for.
```

## Notes

- This is a good intermediate-level prompt that tests multiple skills
- MCP knowledge may vary between AI tools (may need explanation)
- PDF parsing is a common task with multiple library options
- Good test of documentation and code organization abilities

## Contributing

If you implement this prompt with a different AI tool:

1. Add your implementation to `<vendor>/game-rules-pdf-server/`
2. Update the "Implementations" section above with:
   - Tool name and checkmark
   - Implementation location
   - Date completed
   - Language used
   - Key features
   - Libraries used
   - Notable implementation choices
3. Commit with a descriptive message

---

**Created**: 2025-10-22
**Last Updated**: 2025-10-22
**Total Implementations**: 1 (Claude Code)
