# SMELT Scaffold

Public open-core scaffold for SMELT, a production multi-agent AI boilerplate by GIMZWARE.

## What This Repository Is

`smelt-scaffold` is the public marketing/education repository. It provides:

- Project structure and architecture boundaries
- Docker local infrastructure bootstrap (`NATS` + `Redis`)
- Typed schema and orchestrator stub layout
- Decision-driven documentation for extension and adaptation

It intentionally **does not** include the full working agent implementations, full Rust router, or private member-only assets.

## Product Positioning

SMELT is designed for senior Python and AI engineers who want a principled starting point for production multi-agent systems without framework lock-in.

- Tagline: **Smelt your agents into production**
- Philosophy: explicit contracts, explicit state, explicit observability
- Anti-goal: hidden orchestration magic and runtime abstractions

## Public vs Private Scope

### Included Here (Public)

- Scaffolded Python package layout
- Stubbed contracts (`WorkItem`, `WorkResult`, task state models)
- Stubbed agent/orchestrator/memory module boundaries
- Basic local stack bootstrap via Docker Compose
- Architecture notes and design rationale

### Not Included Here

- Working `ResearchAgent`, `ReasoningAgent`, `ActionAgent`
- Full asyncio orchestrator with production task state transitions
- Full Rust router implementation and gRPC bridge
- End-to-end production pipeline with real LLM calls
- Member templates, deployment packs, and premium docs

## Reference Architecture (v1 Intent)

SMELT’s production architecture (implemented in private repo) is layered as:

1. FastAPI ingress (validation + trace stamping)
2. NATS JetStream event bus
3. Python asyncio orchestrator with Pydantic task state machine
4. Worker agents (research, reasoning, action)
5. Memory split by concern:
   - Redis: working memory
   - Postgres: episodic/audit history
   - pgvector: semantic retrieval
6. Rust router for hot-path routing, exposed to Python via gRPC
7. OpenTelemetry + structured logging observability

## Quickstart

```bash
docker compose up
```

This starts the local dependencies expected by the scaffold. Extend the stubs to build your own implementation, or use the private SMELT repo for the complete working version.

## Design Principles

- **No framework lock-in:** no LangGraph-style orchestration dependency
- **Strict contracts:** boundary models validated with strict Pydantic schemas
- **Operational clarity:** decisions are documented so teams can replace components with intent
- **Separation of concerns:** ingress, orchestration, agent execution, memory, and routing are split cleanly

## Roadmap Snapshot

- **v1 (Boilerplate):** scaffold + docs + local stack + baseline contracts
- **v2 (Living Kit):** advanced templates, Temporal workflows, K8s manifests, member support
- **v3 (Smelter):** guided scaffolding tool for custom repo generation

## Get the Full Version

This is the public scaffold. The full working implementation includes:
- 5 domain templates (Customer Support, Content Moderation, Market Research, Data Pipeline, Code Review)
- Studio trace visualiser
- Smelter wizard access
- CLI scaffolding tools

**Get started at [smelt.gimzware.ai](https://smelt.gimzware.ai)**

## Licensing

This repository is distributed under SMELT’s open-core licensing model.

- Public scaffold: source-available under a proprietary view-focused license
- Working implementation: distributed through paid tiers (Starter/Member/Enterprise)

See `LICENCE` for exact terms.
