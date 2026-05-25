"""SMELT entry point - stub for the production orchestrator startup.

The full implementation (available at smelt.gimzware.ai) starts the orchestrator
and all worker agents in a single-process asyncio TaskGroup with:
  - OpenTelemetry tracing and structured logging initialisation
  - NATS JetStream connection and stream provisioning
  - LLMClient construction from environment
  - ResearchAgent, ReasoningAgent, and ActionAgent concurrent startup

Extend the stub modules in smelt.orchestrator, smelt.agents, smelt.memory,
and smelt.observability to build your own implementation.
"""

from __future__ import annotations

import asyncio
import sys


async def run() -> None:
    """Start the SMELT orchestrator and all worker agents.

    Stub: replace with your orchestrator and agent initialisation.
    """
    raise NotImplementedError(
        "smelt.__main__.run() is a stub. "
        "Implement orchestrator and agent startup, or build on the managed "
        "SMELT Studio at https://smelt.gimzware.ai"
    )


def main() -> None:
    """Entry point for the smelt CLI.

    Stub: replace with full startup including uvloop, dotenv, and structlog.
    """
    print(  # noqa: T201
        "SMELT scaffold - this is a stub entry point.\n"
        "Implement run(), or build on the managed SMELT Studio at https://smelt.gimzware.ai",
        file=sys.stderr,
    )
    asyncio.run(run())


if __name__ == "__main__":
    main()
