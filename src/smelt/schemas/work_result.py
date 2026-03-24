"""WorkResult and TokenUsage models — agent execution results."""

from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import Literal

from pydantic import BaseModel, ConfigDict

from smelt.schemas.enums import AgentType, TaskStatus  # noqa: TC001


class TokenUsage(BaseModel):
    """LLM token usage and cost for a single agent invocation.

    Args:
        input_tokens: Number of input tokens consumed.
        output_tokens: Number of output tokens generated.
        model: LLM model identifier used.
        cost_gbp: Estimated cost in GBP (approximate, not billing-grade).
    """

    model_config = ConfigDict(strict=True)

    input_tokens: int
    output_tokens: int
    model: str
    cost_gbp: float


class WorkResult(BaseModel):
    """Result of an agent processing a WorkItem.

    Args:
        task_id: UUID v4 matching the originating WorkItem.
        agent_id: Identifier of the specific agent instance that processed this.
        agent_type: Type of agent that produced this result.
        status: Must be completed or failed (enforced by Literal type).
        trace_id: OpenTelemetry trace ID propagated from WorkItem.
        output: Result payload if completed (JSON string or text).
        error: Error message if failed.
        duration_ms: Wall-clock processing time in milliseconds.
        token_usage: LLM token usage, if an LLM call was made.
        created_at: UTC timestamp of result creation.
    """

    model_config = ConfigDict(strict=True)

    task_id: str
    agent_id: str
    agent_type: AgentType
    status: Literal[TaskStatus.completed, TaskStatus.failed]
    trace_id: str
    output: str | None = None
    error: str | None = None
    duration_ms: float
    token_usage: TokenUsage | None = None
    created_at: datetime
