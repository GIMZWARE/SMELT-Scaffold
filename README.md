# SMELT Scaffold

The open, public reference architecture for **SMELT**, a multi-agent AI platform by GIMZWARE.

This repository shows exactly how SMELT is built: the typed contracts, the module boundaries, and the design decisions behind a real multi-agent system. It is the architecture you own and can inspect. The fastest way to build and run agent workflows on it is the managed product, **SMELT Studio**.

**Build agent workflows visually, run them pay-as-you-go, own the architecture. Start free at [smelt.gimzware.ai](https://smelt.gimzware.ai).**

## Why SMELT

- **No framework lock-in.** No LangGraph, no CrewAI, no hidden orchestration. The contracts and architecture are public (this repo), so you are never trapped.
- **A real multi-agent architecture.** Five specialised agents, a durable NATS event bus, an explicit Pydantic state machine, and four purpose-built memory stores. Not a single-prompt wrapper.
- **Visual builder, managed runtime.** SMELT Studio builds agent workflows on a visual canvas and runs them on managed infrastructure, billed per run.

## What is in this repository

- Project structure and architecture boundaries
- The full typed schema contracts (`WorkItem`, `WorkResult`, `TaskState`, typed payloads), identical to the running engine
- Stubbed agent, orchestrator, and memory module boundaries with documented design rationale
- Local infrastructure bootstrap (NATS + Redis) via Docker Compose

It intentionally does not include the working agent implementations or the Rust router. Those run inside the managed product.

## Reference architecture

SMELT is layered as:

1. FastAPI ingress (validation + trace stamping)
2. NATS JetStream event bus (durable at-least-once delivery)
3. Python asyncio orchestrator with a Pydantic task state machine
4. Five specialised worker agents
5. Memory split by concern:
   - Redis: working memory + shared scratchpad
   - Postgres: episodic and audit history
   - pgvector: semantic retrieval
6. Rust router for hot-path fan-out, exposed to Python via gRPC
7. OpenTelemetry + structlog observability

## Quickstart (inspect and extend the architecture)

```bash
pip install -e ".[dev]"
docker compose up
```

This starts the local dependencies the scaffold expects. Read the stub docstrings to see what each component does, then extend them. Or skip the infrastructure entirely and build on SMELT Studio.

## SMELT Studio

SMELT Studio is the hosted way to build and run agent workflows on this architecture:

- Visual workflow builder
- Managed agents, orchestration, memory, and observability
- Pay-as-you-go: a free tier, then per-run billing

**Start free at [smelt.gimzware.ai](https://smelt.gimzware.ai)**

## Design principles

- **No framework lock-in:** no LangGraph, no CrewAI, no orchestration dependency
- **Strict contracts:** boundary models validated with Pydantic `strict=True`
- **Operational clarity:** decisions are documented so teams can replace components with intent
- **Separation of concerns:** ingress, orchestration, agent execution, memory, and routing are split cleanly
- **Debuggability over magic:** explicit state, explicit routing, explicit observability

## Licensing

This repository is distributed under a proprietary view-only licence. The source is provided for inspection and evaluation. The managed product is SMELT Studio at [smelt.gimzware.ai](https://smelt.gimzware.ai). See `LICENCE` for exact terms.
