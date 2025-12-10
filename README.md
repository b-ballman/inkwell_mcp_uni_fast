# Trinity Lens Fast MCP Server

A streamlined framework injector that applies Trinity Graph thinking efficiently to ANY query. Maintains K/S/G/Convergence structure with faster execution.

## What is Trinity Lens Fast?

Trinity Lens Fast is an MCP (Model Context Protocol) server that provides a **mandatory multi-dimensional thinking framework** for analyzing any query. It ensures that AI responses consider three core dimensions plus their convergence:

- **📊 Knowledge**: Facts, data, research, and constraints
- **👥 Social**: Stakeholders, motivations, relationships, and psychology  
- **💡 Generative**: Patterns, innovations, scenarios, and cross-domain insights
- **🔮 Convergence**: Emergent insights that appear only when K+S+G combine

## Connection URL

```
https://trinity-lens-fast-239479891351.us-central1.run.app/sse
```

## How to Connect

### In Claude Desktop or MCP-Compatible Clients

Add to your MCP configuration file:

```json
{
  "mcpServers": {
    "trinity-lens-fast": {
      "url": "https://trinity-lens-fast-239479891351.us-central1.run.app/sse",
      "transport": "sse"
    }
  }
}
```

## Available Tools

### 1. `analyze_trinity_fast` (MANDATORY)

**Purpose**: Apply the Trinity framework to any query

**Parameters**:
- `query` (required): The question or topic to analyze
- `focus` (optional): Emphasis dimension - `'knowledge'`, `'social'`, `'generative'`, or `'balanced'` (default)

**What it does**: Returns a structured framework template that ensures your AI assistant analyzes the query from all four required perspectives.

### 2. `get_key_terms`

**Purpose**: Get essential abstract terms for Trinity thinking

**Returns**: Key "-ity" terms (authenticity, complexity, serendipity, etc.) that help bridge the K/S/G dimensions in your analysis.

### 3. `quick_convergence_guide`

**Purpose**: Get quick guidance on applying Convergence to a specific topic

**Parameters**:
- `topic` (required): The subject to analyze

**Returns**: Convergence prompts and tips for analyzing how K+S+G dimensions interact for that topic.

## Key Principle

**This MCP is designed to be ALWAYS-ON**: When connected, it should be used for **every** substantive query, not just complex ones. The framework reveals insights that single-dimension thinking misses.

## Example Usage Flow

1. **Connect** the MCP server using the URL above
2. **Ask any question** to your AI assistant
3. The assistant will call `analyze_trinity_fast` with your query
4. You'll receive a structured response covering:
   - Knowledge facts
   - Social/human factors
   - Generative patterns
   - Emergent convergent insights

## Why Use This?

Multi-dimensional thinking reveals:
- **Bridges**: How dimensions inform each other
- **Serendipity**: Unexpected valuable connections
- **Synchronicity**: Independent alignments across dimensions  
- **Emergent Insight**: Understanding impossible from any single dimension alone

The "Fast" version maintains the full K/S/G/Convergence structure while optimizing for speed and conciseness.

## Installation

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python server.py
```

The server will start on port 8000 (or the port specified by the `PORT` environment variable).

## Deployment

This project includes:
- `Dockerfile` for containerization
- `cloudbuild.yaml` for Google Cloud Build deployment

## License

[Add your license here]


