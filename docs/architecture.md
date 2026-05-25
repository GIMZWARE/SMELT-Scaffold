# SMELT Architecture

This document is a brief orientation to the scaffold structure. The README
contains the full reference architecture description.

## Layer Map

```
src/smelt/gateway/       FastAPI ingress - validates TaskRequest, stamps trace_id,
                         publishes WorkItem to NATS.

src/smelt/orchestrator/  Asyncio task state machine - consumes TaskRequest from NATS,
                         manages state transitions, dispatches WorkItem to agent subjects,
                         collects WorkResult and finalises TaskState.

src/smelt/agents/        Worker agents - pull consumers on per-type NATS subjects.
                         ResearchAgent, ReasoningAgent, ActionAgent each implement
                         process(WorkItem[T]) -> WorkResult.

src/smelt/memory/        Storage layer - RedisMemory (working), PostgresMemory (episodic),
                         VectorMemory (semantic retrieval via pgvector).

src/smelt/observability/ OTel tracing + structlog setup. Injects trace/span IDs into
                         all log records.

rust/router/             Hot-path NATS router with gRPC interface. Handles fan-out from
                         smelt.tasks.* to smelt.agents.<type> subjects at Rust throughput.

src/smelt/schemas/       Pydantic contracts shared by all layers. These are FULL in the
                         scaffold - WorkItem, WorkResult, TaskState, TaskRequest, all
                         payload types, enums, and state transition validation.
```

## Stub vs Full

| Module | Scaffold | Full (smelt.gimzware.ai) |
|---|---|---|
| `schemas/` | Full - exact production types | Same |
| `orchestrator/` | Docstring stub | Orchestrator, NatsClient, OrchestratorConfig |
| `agents/` | Docstring stub | BaseAgent, ResearchAgent, ReasoningAgent, ActionAgent |
| `memory/` | Docstring stub | RedisMemory, PostgresMemory, VectorMemory |
| `observability/` | Docstring stub | setup_tracing(), setup_logging(), get_tracer() |
| `gateway/` | Docstring stub | FastAPI app, lifespan, middleware |
| `rust/router/` | Empty main() | Full NATS fan-out router + tonic gRPC server |

## Extending the Scaffold

1. Start `docker compose up` to bring up NATS and Redis.
2. Implement `smelt.orchestrator.NatsClient` - connect, ensure_streams, publish, pull_consumer.
3. Implement `smelt.orchestrator.Orchestrator.run()` - subscribe to TaskRequest, drive state machine.
4. Implement `smelt.agents.BaseAgent` - pull consumer loop, WorkItem deserialisation, WorkResult publish.
5. Implement at least one concrete agent (`ResearchAgent` is the simplest starting point).
6. Wire up `smelt.__main__.run()` with your Orchestrator and agent instances in a TaskGroup.

For the complete working implementation, visit https://smelt.gimzware.ai.
