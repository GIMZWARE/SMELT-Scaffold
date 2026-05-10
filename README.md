# SMELT Scaffold

Public open-core scaffold for SMELT, a production multi-agent AI boilerplate by GIMZWARE.

## What This Repository Is

`smelt-scaffold` is the public reference repository. It provides:

- Project structure and architecture boundaries
- Docker local infrastructure bootstrap (`NATS` + `Redis`)
- Full typed schema contracts (identical to the paid implementation)
- Decision-driven documentation for extension and adaptation

It intentionally **does not** include the full working agent implementations, Rust router, or paid-tier assets.

## Who This Is For

Senior Python and AI engineers who want a principled starting point for production multi-agent systems without framework lock-in.

- Tagline: **Smelt your agents into production**
- Philosophy: explicit contracts, explicit state, explicit observability
- Anti-goal: hidden orchestration magic and runtime abstractions

## Public vs Paid Scope

### Included Here (Public)

- Scaffolded Python package layout
- Full production contracts (`WorkItem`, `WorkResult`, `TaskState`, typed payloads)
- Stubbed agent/orchestrator/memory module boundaries
- Local stack bootstrap via Docker Compose
- Architecture notes and design rationale

### Available with Purchase

- Full working agents — Planner, Research, Reasoning, Action, Validator
- Asyncio orchestrator with intelligent routing and scatter-gather
- Rust NATS router with gRPC bridge
- End-to-end pipeline with real LLM calls
- Domain templates and CLI scaffolding tools
- Studio trace visualiser
- Guardrails middleware and policy-as-code
- MCP and A2A protocol support

More tools and templates are added continuously.

## Reference Architecture

SMELT's production architecture (implemented in the private repo) is layered as:

1. FastAPI ingress (validation + trace stamping)
2. NATS JetStream event bus (durable at-least-once delivery)
3. Python asyncio orchestrator with Pydantic task state machine
4. Five specialised worker agents
5. Memory split by concern:
   - Redis: working memory + shared scratchpad
   - Postgres: episodic/audit history
   - pgvector: semantic retrieval
6. Rust router for hot-path fan-out, exposed to Python via gRPC
7. OpenTelemetry + structlog observability

## Quickstart

```bash
pip install -e ".[dev]"
docker compose up
```

This starts the local dependencies expected by the scaffold. Extend the stubs to build your own implementation, or purchase the full working version.

## Design Principles

- **No framework lock-in:** no LangGraph, no CrewAI, no orchestration dependency
- **Strict contracts:** boundary models validated with Pydantic `strict=True`
- **Operational clarity:** decisions are documented so teams can replace components with intent
- **Separation of concerns:** ingress, orchestration, agent execution, memory, and routing are split cleanly
- **Debuggability over magic:** explicit state, explicit routing, explicit observability

## Get the Full Version

This is the public scaffold. The full working implementation includes everything listed above plus ongoing updates and support.

**Get started at [smelt.gimzware.ai](https://smelt.gimzware.ai)**

## Licensing

This repository is distributed under a proprietary view-only licence. The source is provided for inspection and evaluation only. The working implementation is available through paid plans on the SMELT site.

See `LICENCE` for exact terms.
