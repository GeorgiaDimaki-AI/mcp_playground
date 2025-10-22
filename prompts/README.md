# Prompts Directory

This directory contains vendor-agnostic prompts used to generate projects in this playground. Each prompt can be used with any AI coding tool to enable fair comparisons.

## Purpose

By documenting prompts in a central, vendor-agnostic location:
- **Reproducibility**: Anyone can try the same prompt with different AI tools
- **Fair Comparison**: Same starting point for all implementations
- **Learning**: Understand how different AI tools interpret requirements
- **Cross-Vendor Tracking**: One prompt file tracks all implementations across vendors
- **No Duplication**: Single source of truth for each prompt

## Structure

Each prompt is a separate markdown file in this directory containing:
- The original prompt (verbatim)
- A structured version with clear requirements
- List of ALL implementations (across all vendors)
- Comparison criteria and evaluation framework
- Variations to try

## Available Prompts

### 1. Game Rules PDF Server

**File**: [game-rules-pdf-server.md](game-rules-pdf-server.md)

**Type**: MCP Server | **Difficulty**: Intermediate

**Summary**: Create an MCP server for querying game rules from PDF files

**Implementations**:
- ✅ Claude Code → [claude_code/game-rules-pdf-server/](../claude_code/game-rules-pdf-server/)
- ⏳ Cursor → *Try it and add your implementation!*
- ⏳ GitHub Copilot → *Try it and add your implementation!*
- ⏳ Other tools → *Try it and add your implementation!*

**Skills Tested**: PDF parsing, MCP protocol, API design, documentation

---

## How to Use These Prompts

### For Trying a New Implementation

1. **Choose a prompt** from the list above
2. **Open the prompt file** (e.g., `game-rules-pdf-server.md`)
3. **Copy the prompt** (original or structured version)
4. **Open your AI coding tool** (Cursor, Copilot, etc.)
5. **Paste and run** the prompt
6. **Save the implementation** to `<vendor>/<project-name>/`
7. **Update the prompt file** with your implementation details

### For Comparing Implementations

1. **Pick a prompt** that has multiple implementations
2. **Review each implementation** in different vendor folders
3. **Use the comparison criteria** in the prompt file
4. **Document interesting differences** or insights

## Adding New Prompts

When you create a new project in the playground:

1. **Create a prompt file**: `prompts/<project-name>.md`
2. **Use this template structure**:
   ```markdown
   # Prompt: Project Name

   ## The Prompt
   ### Original Request
   (your exact words)

   ### Structured Version
   (clear requirements)

   ## Implementations
   ### ✅ Tool Name
   - Location: ...
   - Features: ...

   ## Comparison Criteria
   (what to compare)
   ```
3. **Add to this README** in the "Available Prompts" section
4. **Reference from your project** README back to the central prompt

## Comparison Framework

The prompts include detailed comparison criteria, but generally evaluate:

### Functionality
- Core requirements met
- Additional features
- Missing features
- Edge case handling

### Code Quality
- Project structure
- Readability
- Error handling
- Type safety
- Testing

### Documentation
- README completeness
- Setup instructions
- Usage examples
- Code comments
- Troubleshooting

### Developer Experience
- Installation ease
- Dependencies
- Configuration
- Time to first run

### User Experience
- Feature discoverability
- Error messages
- Performance
- Reliability

## Contributing Your Implementations

If you implement a prompt with a different AI tool:

1. **Create vendor folder** if it doesn't exist (e.g., `cursor/`)
2. **Create project folder** matching the prompt name
3. **Add your implementation**
4. **Update the prompt file** with:
   - Tool name and status (✅)
   - Implementation location
   - Date and language used
   - Key features and notable choices
5. **Update this README** if adding a new tool
6. **Commit with description** of your implementation

## Why This Structure?

**Before** (vendor-specific prompts):
```
claude_code/project/PROMPT.md  ← Claude's prompt
cursor/project/PROMPT.md        ← Cursor's prompt (duplicate!)
```
Problem: Prompts drift, hard to compare, duplication

**After** (central prompts):
```
prompts/project.md              ← Single source of truth
  ├─ Lists: claude_code/project/
  └─ Lists: cursor/project/
```
Benefits: No duplication, easy comparison, tracks all implementations

---

**Last Updated**: 2025-10-22
**Total Prompts**: 1
**Total Implementations**: 1

**Remember**: The goal is learning and comparison, not competition. Each AI tool has different strengths, and the "best" implementation depends on your specific needs and preferences.
