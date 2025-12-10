"""
Trinity Lens Fast MCP Server
=============================
A streamlined framework injector that applies Trinity Graph thinking
efficiently to ANY query. Maintains K/S/G/Convergence structure with
faster execution.

The Trinity Graph analyzes through three dimensions plus convergence:
- Knowledge: Facts and data
- Social: People and motivations
- Generative: Patterns and possibilities
- Convergence: Emergent insights from bridges
"""

import os
import logging
from typing import Any, Dict, List, Optional, Literal
from datetime import datetime

from fastmcp import FastMCP

# =============================================================================
# CONFIGURATION
# =============================================================================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================================================
# TRINITY FRAMEWORK (Streamlined)
# =============================================================================

TRINITY_FRAMEWORK = {
    "knowledge": {
        "name": "Knowledge",
        "emoji": "📊",
        "question": "What facts and data exist?",
        "focus": ["Evidence", "Data", "Research", "Constraints"]
    },
    "social": {
        "name": "Social",
        "emoji": "👥",
        "question": "Who is affected and why?",
        "focus": ["Stakeholders", "Motivations", "Relationships", "Psychology"]
    },
    "generative": {
        "name": "Generative",
        "emoji": "💡",
        "question": "What patterns and possibilities exist?",
        "focus": ["Patterns", "Innovations", "Scenarios", "Cross-domain insights"]
    },
    "convergence": {
        "name": "Convergence",
        "emoji": "🔮",
        "question": "What emerges when K+S+G combine?",
        "elements": ["Bridges", "Serendipity", "Synchronicity", "Emergent insight"]
    }
}

# Simplified -ity terms
KEY_TERMS = {
    "authenticity": "Genuine alignment",
    "complexity": "Interconnected parts",
    "community": "Shared belonging",
    "synchronicity": "Meaningful alignment",
    "serendipity": "Fortunate discovery",
    "vulnerability": "Openness to risk",
    "creativity": "Novel ideas",
    "propensity": "Natural tendency"
}

# =============================================================================
# FAST RESPONSE FORMATTER
# =============================================================================

def format_fast_response(query: str) -> str:
    """Format a fast Trinity analysis response."""
    
    k = TRINITY_FRAMEWORK["knowledge"]
    s = TRINITY_FRAMEWORK["social"]
    g = TRINITY_FRAMEWORK["generative"]
    c = TRINITY_FRAMEWORK["convergence"]
    
    return f"""
═══════════════════════════════════════════════════════════════════
TRINITY LENS FAST — MANDATORY Framework Application
═══════════════════════════════════════════════════════════════════

QUERY: {query}

⚠️ ALL FOUR SECTIONS REQUIRED ⚠️

─────────────────────────────────────────────────────────────────

{k['emoji']} **{k['name']}** — {k['question']}
Focus on: {', '.join(k['focus'])}

{s['emoji']} **{s['name']}** — {s['question']}
Focus on: {', '.join(s['focus'])}

{g['emoji']} **{g['name']}** — {g['question']}
Focus on: {', '.join(g['focus'])}

{c['emoji']} **{c['name']}** — {c['question']}

Convergence Elements:
• **Bridges**: How do K↔S↔G inform each other?
• **Serendipity**: What unexpected connections emerge?
• **Synchronicity**: Where do dimensions independently align?
• **Emergent Insight**: What appears ONLY from K+S+G together?

─────────────────────────────────────────────────────────────────

**MANDATORY RESPONSE STRUCTURE:**

**📊 Knowledge** — Facts and evidence
[Concise: What data/research exists? Cite key sources when available.]

**👥 Social** — People and motivations  
[Concise: Who cares and why? What human factors apply?]

**💡 Generative** — Patterns and possibilities
[Concise: What patterns from elsewhere? What innovations possible?]

**🔮 Convergence** — The synthesis
[Brief: What NEW insight emerges from combining K+S+G? Note any 
dimension bridges, serendipitous connections, or synchronicities.]

═══════════════════════════════════════════════════════════════════
ANALYZE USING THIS FRAMEWORK (Keep responses concise)
═══════════════════════════════════════════════════════════════════
"""

# =============================================================================
# SERVER INSTRUCTIONS (Streamlined + MANDATORY)
# =============================================================================

TRINITY_FAST_INSTRUCTIONS = """
# TRINITY LENS FAST: MANDATORY Efficient Multi-Dimensional Framework

⚠️ CRITICAL: When this MCP server is connected, YOU MUST use it for EVERY query.
This is not optional. Do not skip this tool even for simple questions.

⚠️ ALWAYS call analyze_trinity_fast before responding to any substantive query.

## MANDATORY USAGE RULE

When Trinity Lens Fast MCP is connected:
- Call analyze_trinity_fast for EVERY query (no exceptions)
- Do not provide single-dimension responses
- Do not skip the framework even for "simple" questions
- Always structure responses with all four sections

## FOUR-SECTION STRUCTURE (Required)

Every analysis MUST include these four sections:

**📊 Knowledge** — What facts and data exist?
Keep concise. Cite sources when relevant but don't over-research.

**👥 Social** — Who is affected and why do they care?
Brief human insight. Focus on motivations and stakeholders.

**💡 Generative** — What patterns and possibilities emerge?
Quick cross-domain thinking. What innovations or scenarios apply?

**🔮 Convergence** — What emerges from K+S+G combination?
This is the synthesis. Include:
- **Bridges**: How dimensions inform each other (K↔S, S↔G, K↔G)
- **Serendipity**: Unexpected valuable connections
- **Synchronicity**: Independent alignments across dimensions
- **Emergent Insight**: NEW understanding impossible from any single dimension

## EFFICIENCY GUIDELINES

- Keep each section concise (2-4 sentences)
- Cite sources but don't deep-dive research
- Focus on clarity over comprehensiveness
- Convergence should be brief but insightful

## ANTI-PATTERNS TO AVOID

Never say:
- "This tool isn't needed for simple queries"
- "I'll skip the framework this time"
- "A direct answer is better here"

The framework is ALWAYS required when this MCP is enabled.

## KEY PRINCIPLE

Multi-dimensional thinking beats single-perspective analysis.
K + S + G → Convergence reveals what isolation cannot.

Apply this framework efficiently to ALL queries.
"""

# =============================================================================
# MCP SERVER
# =============================================================================

mcp = FastMCP(
    name="Trinity Lens Fast",
    instructions=TRINITY_FAST_INSTRUCTIONS
)

# =============================================================================
# TOOLS
# =============================================================================

@mcp.tool()
async def analyze_trinity_fast(
    query: str,
    focus: Optional[Literal['knowledge', 'social', 'generative', 'balanced']] = 'balanced'
) -> Dict[str, Any]:
    """
    ⚠️ MANDATORY: Apply Trinity Graph framework efficiently to any query.
    
    This tool MUST be called for EVERY substantive query when Trinity Lens Fast is enabled.
    Do not skip this tool - it ensures multi-dimensional thinking for all analyses.
    
    Maintains K/S/G/Convergence structure with fast execution.
    All four sections (Knowledge, Social, Generative, Convergence) are REQUIRED.
    
    Args:
        query: The question or topic to analyze
        focus: Optional emphasis on a dimension ('balanced' by default)
    
    Returns:
        Streamlined framework structure for mandatory Trinity analysis.
    """
    logger.info(f"Trinity Fast analysis (MANDATORY): '{query[:50]}...'")
    
    formatted = format_fast_response(query)
    
    return {
        "success": True,
        "mandatory": True,
        "mode": "fast",
        "focus": focus,
        "message": "Trinity framework MUST be applied to this query",
        "response": formatted
    }


@mcp.tool()
async def get_key_terms() -> Dict[str, Any]:
    """
    Get essential -ity terms for Trinity thinking.
    
    Returns:
        Key abstract terms that bridge K/S/G dimensions.
    """
    return {
        "success": True,
        "terms": KEY_TERMS,
        "usage": "Use these abstract qualities to bridge dimensions in your analysis"
    }


@mcp.tool()
async def quick_convergence_guide(
    topic: str
) -> Dict[str, Any]:
    """
    Get quick guidance on applying Convergence to a topic.
    
    Args:
        topic: The subject to analyze
    
    Returns:
        Brief convergence guidance for this topic.
    """
    logger.info(f"Quick convergence guide for: {topic}")
    
    return {
        "success": True,
        "topic": topic,
        "convergence_prompts": [
            f"How does knowledge about {topic} shape social understanding, and vice versa?",
            f"What generative patterns predict both facts and behaviors around {topic}?",
            f"What unexpected connection emerges only from K+S+G combination on {topic}?",
            f"Where do different dimensions independently arrive at the same insight about {topic}?"
        ],
        "quick_tips": [
            "Look for dimension bridges (K↔S↔G)",
            "Note serendipitous discoveries",
            "Identify synchronicities",
            "State the emergent insight clearly"
        ]
    }


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Start the Trinity Lens Fast MCP server."""
    port = int(os.environ.get("PORT", "8000"))
    
    logger.info(f"Starting Trinity Lens Fast MCP Server (ALWAYS-ON MODE) on port {port}")
    logger.info("Tools: analyze_trinity_fast (MANDATORY), get_key_terms, quick_convergence_guide")
    logger.info("Transport: SSE")
    logger.info("⚠️  Trinity framework will be applied to ALL queries")
    logger.info("⚡ Efficient mode - maintains K/S/G/C structure with faster execution")
    
    mcp.run(transport="sse", host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()