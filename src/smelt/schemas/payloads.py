"""Per-agent payload models for WorkItem parameterisation."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ResearchPayload(BaseModel):
    """Payload for ResearchAgent - RAG retrieval and web search.

    Args:
        query: The research question or topic to investigate.
        max_sources: Maximum number of sources to retrieve.
        search_web: Whether to include web search results.
    """

    model_config = ConfigDict(strict=True)

    query: str
    max_sources: int = 5
    search_web: bool = False


class ReasoningPayload(BaseModel):
    """Payload for ReasoningAgent - chain-of-thought and self-consistency.

    Args:
        prompt: The reasoning prompt or question.
        context: Supporting context strings from prior agent outputs.
        voting_rounds: Number of parallel completions for self-consistency voting.
    """

    model_config = ConfigDict(strict=True)

    prompt: str
    context: list[str] = Field(default_factory=list)
    voting_rounds: int = 1


class ActionPayload(BaseModel):
    """Payload for ActionAgent - external tool calls and side effects.

    Args:
        tool_name: Name of the tool to invoke.
        parameters: Key-value parameters for the tool call.
        requires_approval: Whether this action needs PendingApproval gate.
    """

    model_config = ConfigDict(strict=True)

    tool_name: str
    parameters: dict[str, str] = Field(default_factory=dict)
    requires_approval: bool = False


class GenericPayload(BaseModel):
    """Escape hatch for rapid prototyping. Accepts arbitrary fields.

    Use this when defining a new agent type before committing to a typed payload.
    Migrate to a dedicated payload model before production use.
    """

    model_config = ConfigDict(strict=True, extra="allow")
