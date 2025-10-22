# Claude Code Projects

This folder contains projects built using **Claude Code**, Anthropic's official CLI tool for Claude.

## About Claude Code

[Claude Code](https://claude.com/claude-code) is an interactive CLI tool that helps with software engineering tasks. It excels at:

- Full-stack development
- Reading and understanding large codebases
- Creating well-structured, documented projects
- Following best practices and conventions
- Working with modern frameworks and tools

## Projects in This Folder

### 1. game-rules-pdf-server

**Status**: ✅ Complete
**Type**: MCP Server
**Language**: Python
**Created**: 2025-10-22

An MCP (Model Context Protocol) server that enables AI assistants to query game rules from PDF files.

**Features:**
- Resources: Expose game rulebooks as MCP resources
- Tools: list_games, search_game_rules, get_game_summary
- PDF parsing with PyPDF2
- Context-aware search functionality
- Full documentation and quick start guide

**Use Case:**
Perfect for board game enthusiasts who want to quickly look up rules without manually searching through PDF rulebooks. Ask your AI assistant questions like "What are the rules for castling in chess?" and get instant answers from the actual rulebooks.

**Location**: [game-rules-pdf-server/](game-rules-pdf-server/)

**Documentation**: [game-rules-pdf-server/README.md](game-rules-pdf-server/README.md)

---

## Claude Code's Strengths Demonstrated

These projects showcase several strengths of Claude Code:

1. **Comprehensive Documentation**: Each project includes detailed READEs, quick start guides, and examples
2. **Project Structure**: Well-organized code with clear separation of concerns
3. **Error Handling**: Robust error handling and helpful error messages
4. **Best Practices**: Follows Python conventions, proper typing, and async patterns
5. **User Focus**: Includes example configs, setup instructions, and troubleshooting sections

## Project Ideas for Future Development

Here are some ideas for additional Claude Code projects:

- **Code Review MCP Server**: Automated code review suggestions
- **Documentation Generator**: Generate docs from code comments
- **Test Generator**: Create unit tests for existing code
- **API Client Generator**: Generate API clients from OpenAPI specs
- **Database Schema Visualizer**: MCP server for exploring database schemas
- **Git History Analyzer**: Analyze commit patterns and code churn

## Development Workflow

Projects in this folder were created using Claude Code's interactive workflow:

1. **Planning**: Claude Code helps break down requirements
2. **Implementation**: Writes clean, well-documented code
3. **Testing**: Suggests tests and validates syntax
4. **Documentation**: Creates comprehensive documentation
5. **Git Integration**: Handles commits with proper messages

## Getting Started

Each project has its own setup instructions. Generally:

1. Navigate to the project folder
2. Read the project's README.md
3. Install dependencies
4. Follow the quick start guide

## Notes

- All projects use modern Python (3.10+)
- MCP projects follow the official MCP SDK patterns
- Code is formatted for readability and maintainability
- Documentation is written for both technical and non-technical users

---

**Maintained by**: Claude Code experiments
**Last Updated**: 2025-10-22
**Project Count**: 1
