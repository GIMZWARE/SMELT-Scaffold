# SMELT Scaffold

A small public starter for the typed contracts and module layout of the SMELT engine. SMELT is a multi-agent AI platform by GIMZWARE.

This repository exists so the community can read the contracts, optionally use it as a local starting point, and contribute. It is not the product. The product is the hosted SMELT Studio, a SaaS for building and running agent workflows: [smelt.gimzware.ai](https://smelt.gimzware.ai).

## What is in this repository

- The typed schema contracts (`WorkItem`, `WorkResult`, `TaskState`, typed payloads) used by the engine
- Stubbed agent, orchestrator, and memory module boundaries with design notes
- A local infrastructure bootstrap (NATS and Redis) via Docker Compose

It does not include the working agent implementations or the Rust router; those run inside the hosted product.

## Architecture at a glance

1. FastAPI ingress (validation and trace stamping)
2. NATS JetStream event bus (durable at-least-once delivery)
3. Python asyncio orchestrator with a Pydantic task state machine
4. Specialised worker agents
5. Memory split by concern: Redis (working memory), Postgres (episodic and audit history), pgvector (semantic retrieval)
6. Rust router for hot-path fan-out, exposed to Python over gRPC
7. OpenTelemetry and structlog observability

## Quickstart

```bash
pip install -e ".[dev]"
docker compose up
```

This starts the local dependencies the scaffold expects. Read the stub docstrings to see what each component does, then extend them.

## Design notes

- Strict contracts: boundary models validated with Pydantic `strict=True`
- Separation of concerns: ingress, orchestration, agent execution, memory, and routing are split cleanly
- Explicit over implicit: explicit state, explicit routing, explicit observability

## Contributing

Issues and pull requests are welcome. Please keep changes consistent with the existing contracts and module boundaries.

## SMELT Studio

SMELT Studio is the hosted product for building and running agent workflows: a visual builder with managed agents, orchestration, memory, and observability. It is billed as a monthly subscription with a free tier. See [smelt.gimzware.ai](https://smelt.gimzware.ai).

## Licence

This repository is distributed under a proprietary view-only licence; the source is provided for inspection. See `LICENCE` for the exact terms.
