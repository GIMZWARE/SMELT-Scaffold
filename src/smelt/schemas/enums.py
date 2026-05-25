"""Task status and agent type enums with state transition validation."""

from __future__ import annotations

from enum import StrEnum


class TaskStatus(StrEnum):
    """Status of a task in the orchestration pipeline."""

    pending = "pending"
    dispatched = "dispatched"
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"


class AgentType(StrEnum):
    """Agent types available in the worker pool."""

    research = "research"
    reasoning = "reasoning"
    action = "action"


TERMINAL_STATUSES: frozenset[TaskStatus] = frozenset(
    {
        TaskStatus.completed,
        TaskStatus.failed,
        TaskStatus.cancelled,
    }
)

VALID_TRANSITIONS: dict[TaskStatus, frozenset[TaskStatus]] = {
    TaskStatus.pending: frozenset({TaskStatus.dispatched, TaskStatus.cancelled}),
    TaskStatus.dispatched: frozenset(
        {
            TaskStatus.in_progress,
            TaskStatus.completed,
            TaskStatus.failed,
            TaskStatus.cancelled,
        }
    ),
    TaskStatus.in_progress: frozenset(
        {
            TaskStatus.completed,
            TaskStatus.failed,
            TaskStatus.cancelled,
        }
    ),
    TaskStatus.completed: frozenset(),
    TaskStatus.failed: frozenset(),
    TaskStatus.cancelled: frozenset(),
}


def validate_transition(current: TaskStatus, target: TaskStatus) -> None:
    """Validate a state transition. Raises ValueError if invalid.

    Args:
        current: The current task status.
        target: The desired next status.

    Raises:
        ValueError: If the transition is not allowed.
    """
    if target not in VALID_TRANSITIONS[current]:
        allowed = ", ".join(s.value for s in VALID_TRANSITIONS[current]) or "none (terminal state)"
        msg = f"Invalid transition: {current.value} -> {target.value}. Allowed: {allowed}"
        raise ValueError(msg)
