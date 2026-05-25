"""TaskState model - full lifecycle record stored in episodic memory."""

from __future__ import annotations

from datetime import datetime  # noqa: TC003
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from smelt.schemas.enums import AgentType, TaskStatus  # noqa: TC001
from smelt.schemas.work_result import WorkResult  # noqa: TC001


class TaskState(BaseModel):
    """Full lifecycle record of a task, stored in Postgres episodic memory.

    Args:
        task_id: UUID v4 string.
        status: Current task status.
        agent_type: Type of agent assigned to this task.
        created_at: UTC timestamp of task creation.
        updated_at: UTC timestamp of last status change.
        dispatched_at: When the WorkItem was sent to an agent.
        completed_at: When the final WorkResult was received.
        work_results: List of WorkResults (bounded by MAX_RETRIES).
        total_cost_gbp: Sum of all agent invocation costs.
        total_duration_ms: Sum of all agent processing times.
    """

    model_config = ConfigDict(strict=True)

    MAX_RETRIES: ClassVar[int] = 5

    task_id: str
    status: TaskStatus
    agent_type: AgentType
    created_at: datetime
    updated_at: datetime
    dispatched_at: datetime | None = None
    completed_at: datetime | None = None
    work_results: list[WorkResult] = Field(default_factory=list)
    total_cost_gbp: float = 0.0
    total_duration_ms: float = 0.0
