# Prompts Directory

This directory contains the prompts used to generate projects in this playground. These prompts enable fair comparisons across different AI coding tools.

## Purpose

By documenting the original prompts:
- **Reproducibility**: Others can try the same prompt with different AI tools
- **Fair Comparison**: Same starting point for all implementations
- **Learning**: Understand how different AI tools interpret requirements
- **Experimentation**: Modify prompts to test different approaches

## Available Prompts

### Game Rules PDF Server

**File**: See [claude_code/game-rules-pdf-server/PROMPT.md](../claude_code/game-rules-pdf-server/PROMPT.md)

**Summary**: Create an MCP server for querying game rules from PDF files

**Implemented By**:
- ✅ Claude Code - [claude_code/game-rules-pdf-server/](../claude_code/game-rules-pdf-server/)

**Try with**:
- Cursor
- GitHub Copilot
- Codeium
- Other AI coding tools

## How to Use These Prompts

1. **Choose a prompt** from the list above
2. **Open your AI coding tool** (Cursor, Copilot, etc.)
3. **Copy the structured prompt** from the PROMPT.md file
4. **Let the AI generate** the implementation
5. **Compare results** with existing implementations
6. **Document your findings** (optional but encouraged!)

## Adding New Prompts

When adding a new project to the playground:

1. Create a `PROMPT.md` file in the project directory
2. Include:
   - Original request (verbatim)
   - Structured version
   - Date and AI tool used
   - Implementation notes
3. Reference it in this README
4. Tag it with which tools have implemented it

## Comparison Framework

When comparing implementations, consider:

### Functionality
- Does it meet the core requirements?
- What additional features were added?
- Are there any missing features?

### Code Quality
- Project structure and organization
- Code readability and maintainability
- Error handling
- Type hints and validation

### Documentation
- README quality and completeness
- Code comments
- Setup instructions
- Examples and usage guides

### User Experience
- Ease of installation
- Configuration complexity
- Error messages
- Example files and templates

### Development Process
- Time to completion
- Number of iterations needed
- Questions asked by the AI
- Issues encountered

## Contributing

This is a personal playground, but if you try these prompts with other AI tools:

1. Create a new vendor folder (e.g., `cursor/`, `copilot/`)
2. Implement the project there
3. Document which prompt you used
4. Note any variations or clarifications needed

---

**Remember**: The goal is learning and comparison, not competition. Each AI tool has different strengths, and the "best" implementation depends on your specific needs and preferences.
