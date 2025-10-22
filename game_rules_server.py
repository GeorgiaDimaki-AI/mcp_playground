#!/usr/bin/env python3
"""
Game Rules MCP Server

This MCP server provides access to game rule PDFs, allowing users to:
- List available game rule PDFs
- Read full content of game rules
- Search for specific rules or keywords within games
"""

import os
import sys
from pathlib import Path
from typing import Optional
import PyPDF2
from mcp.server import Server
from mcp.types import Resource, Tool, TextContent, ImageContent, EmbeddedResource
from pydantic import AnyUrl
import mcp.server.stdio


# Directory where game rule PDFs are stored
GAME_RULES_DIR = Path(__file__).parent / "game_rules"


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = []

            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()
                text_content.append(f"--- Page {page_num} ---\n{text}\n")

            return "\n".join(text_content)
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def search_in_pdf(pdf_path: Path, query: str, case_sensitive: bool = False) -> list[dict]:
    """Search for a query string within a PDF and return matching sections."""
    try:
        results = []
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            search_query = query if case_sensitive else query.lower()

            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()
                search_text = text if case_sensitive else text.lower()

                if search_query in search_text:
                    # Find context around the match
                    lines = text.split('\n')
                    matching_lines = []

                    for i, line in enumerate(lines):
                        check_line = line if case_sensitive else line.lower()
                        if search_query in check_line:
                            # Get context: 2 lines before and after
                            start = max(0, i - 2)
                            end = min(len(lines), i + 3)
                            context = '\n'.join(lines[start:end])
                            matching_lines.append({
                                'line_num': i + 1,
                                'context': context
                            })

                    if matching_lines:
                        results.append({
                            'page': page_num,
                            'matches': matching_lines
                        })

        return results
    except Exception as e:
        return [{'error': str(e)}]


def get_available_games() -> list[Path]:
    """Get list of all PDF files in the game rules directory."""
    if not GAME_RULES_DIR.exists():
        GAME_RULES_DIR.mkdir(parents=True, exist_ok=True)
        return []

    return sorted(GAME_RULES_DIR.glob("*.pdf"))


# Initialize the MCP server
app = Server("game-rules-server")


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List all available game rule PDFs as resources."""
    resources = []

    for pdf_file in get_available_games():
        game_name = pdf_file.stem.replace('_', ' ').replace('-', ' ').title()
        resources.append(
            Resource(
                uri=AnyUrl(f"game://{pdf_file.stem}"),
                name=f"{game_name} Rules",
                mimeType="text/plain",
                description=f"Complete rules for {game_name}"
            )
        )

    return resources


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read the full content of a game rules PDF."""
    # Extract game name from URI (format: game://game-name)
    game_name = str(uri).replace("game://", "")
    pdf_path = GAME_RULES_DIR / f"{game_name}.pdf"

    if not pdf_path.exists():
        raise ValueError(f"Game rules not found: {game_name}")

    text_content = extract_text_from_pdf(pdf_path)
    return text_content


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for querying game rules."""
    return [
        Tool(
            name="search_game_rules",
            description="Search for specific text or rules within a game's rulebook. "
                       "Returns relevant sections with context.",
            inputSchema={
                "type": "object",
                "properties": {
                    "game": {
                        "type": "string",
                        "description": "Name of the game (without .pdf extension)"
                    },
                    "query": {
                        "type": "string",
                        "description": "Text to search for in the rules"
                    },
                    "case_sensitive": {
                        "type": "boolean",
                        "description": "Whether the search should be case-sensitive",
                        "default": False
                    }
                },
                "required": ["game", "query"]
            }
        ),
        Tool(
            name="list_games",
            description="List all available game rulebooks in the system.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_game_summary",
            description="Get a summary of a game's rules including page count and basic info.",
            inputSchema={
                "type": "object",
                "properties": {
                    "game": {
                        "type": "string",
                        "description": "Name of the game (without .pdf extension)"
                    }
                },
                "required": ["game"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls for game rules operations."""

    if name == "list_games":
        games = get_available_games()
        if not games:
            return [TextContent(
                type="text",
                text="No game rulebooks found. Please add PDF files to the 'game_rules' directory."
            )]

        game_list = "\n".join([
            f"- {pdf.stem.replace('_', ' ').replace('-', ' ').title()}"
            for pdf in games
        ])
        return [TextContent(
            type="text",
            text=f"Available game rulebooks:\n{game_list}"
        )]

    elif name == "search_game_rules":
        game = arguments.get("game")
        query = arguments.get("query")
        case_sensitive = arguments.get("case_sensitive", False)

        if not game or not query:
            return [TextContent(
                type="text",
                text="Error: Both 'game' and 'query' parameters are required."
            )]

        pdf_path = GAME_RULES_DIR / f"{game}.pdf"
        if not pdf_path.exists():
            return [TextContent(
                type="text",
                text=f"Error: Game rulebook not found: {game}.pdf"
            )]

        results = search_in_pdf(pdf_path, query, case_sensitive)

        if not results:
            return [TextContent(
                type="text",
                text=f"No matches found for '{query}' in {game} rules."
            )]

        # Format results
        output = [f"Search results for '{query}' in {game} rules:\n"]
        for result in results:
            if 'error' in result:
                output.append(f"Error: {result['error']}")
            else:
                output.append(f"\n=== Page {result['page']} ===")
                for match in result['matches']:
                    output.append(f"\n{match['context']}\n")

        return [TextContent(type="text", text="\n".join(output))]

    elif name == "get_game_summary":
        game = arguments.get("game")

        if not game:
            return [TextContent(
                type="text",
                text="Error: 'game' parameter is required."
            )]

        pdf_path = GAME_RULES_DIR / f"{game}.pdf"
        if not pdf_path.exists():
            return [TextContent(
                type="text",
                text=f"Error: Game rulebook not found: {game}.pdf"
            )]

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                page_count = len(pdf_reader.pages)

                # Try to get metadata
                metadata = pdf_reader.metadata
                title = metadata.get('/Title', 'N/A') if metadata else 'N/A'
                author = metadata.get('/Author', 'N/A') if metadata else 'N/A'

                # Get first page excerpt
                first_page = pdf_reader.pages[0].extract_text()[:500]

                summary = f"""Game: {game.replace('_', ' ').replace('-', ' ').title()}
File: {pdf_path.name}
Pages: {page_count}
Title: {title}
Author: {author}

First page excerpt:
{first_page}..."""

                return [TextContent(type="text", text=summary)]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"Error reading PDF: {str(e)}"
            )]

    else:
        return [TextContent(
            type="text",
            text=f"Unknown tool: {name}"
        )]


async def main():
    """Run the MCP server."""
    # Ensure game rules directory exists
    GAME_RULES_DIR.mkdir(parents=True, exist_ok=True)

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
