# CLAUDE.md - SMELT Scaffold

This file provides guidance to Claude Code when working in the smelt-scaffold repository.

## What This Repository Is

`smelt-scaffold` is a **public starter** for SMELT, a multi-agent AI platform by GIMZWARE. It
publishes the typed contracts and module boundaries so the community can read them, optionally
start a local project, and contribute; it is not the working implementation and is not the
product. It is not open-core and should not be advertised as a product.

The product is the hosted SaaS, SMELT Studio (monthly subscription with a free tier), at
https://smelt.gimzware.ai. The working engine runs inside it.

## Repository Structure

```
smelt-scaffold/
  README.md              Public-facing product description and quickstart
  CLAUDE.md              This file
  LICENCE                Proprietary view-only licence
  docker-compose.yml     Local infrastructure bootstrap (NATS + Redis only)
  pyproject.toml         Package metadata and dependency declarations
  .env.example           Environment variable documentation
  .gitignore             Standard Python + Rust ignores
  src/smelt/
    __init__.py           Package version
    __main__.py           Stub CLI entry point
    schemas/              FULL production contracts (see below)
    orchestrator/         Stub - docstring describes private implementation
    agents/               Stub - docstring describes private implementation
    memory/               Stub - docstring describes private implementation
    observability/        Stub - docstring describes private implementation
    gateway/              Stub - docstring describes private implementation
  rust/router/
    Cargo.toml            Full dependency declarations
    src/main.rs           Stub main() with architecture docstring
  docs/
    architecture.md       Layer map and extension guide
```

## Stub vs Full

| Module | This repo | Private repo |
|---|---|---|
| `src/smelt/schemas/` | **FULL** - exact production types | Same |
| `src/smelt/orchestrator/` | Stub docstring only | Full orchestrator, NATS client, config |
| `src/smelt/agents/` | Stub docstring only | BaseAgent + 5 concrete agents |
| `src/smelt/memory/` | Stub docstring only | Redis, Postgres, pgvector implementations |
| `src/smelt/observability/` | Stub docstring only | OTel setup + structlog |
| `src/smelt/gateway/` | Stub docstring only | FastAPI app + lifespan + middleware |
| `rust/router/src/main.rs` | Empty main() | Full NATS fan-out + tonic gRPC server |

## Schemas Are the Source of Truth

The `src/smelt/schemas/` package is the one module that is **identical between the scaffold
and the private repo**. These are the agent contracts published here and run by the managed SMELT Studio:

- `enums.py` - `TaskStatus`, `AgentType`, `VALID_TRANSITIONS`, `validate_transition()`
- `payloads.py` - `ResearchPayload`, `ReasoningPayload`, `ActionPayload`, `GenericPayload`
- `work_item.py` - `WorkItem[T]` generic Pydantic model
- `work_result.py` - `WorkResult`, `TokenUsage`
- `task_state.py` - `TaskState` with `MAX_RETRIES = 5`
- `task_request.py` - `TaskRequest` (external-facing submission contract)

**Do not add implementation logic to the schemas package.** It must remain pure Pydantic
contracts with no I/O, no agent logic, and no infrastructure dependencies.

## Extending the Stubs

To use this scaffold as a starting point for your own implementation:

1. Read the docstring in each stub `__init__.py` - it describes exactly what the private
   version contains and what interface to implement.
2. Create concrete modules alongside each stub (e.g., `orchestrator/orchestrator.py`,
   `agents/base.py`). Do not modify the stub `__init__.py` itself - keep it as reference.
3. Wire your implementations into `__main__.py` `run()`.
4. Run `docker compose up` to start NATS and Redis before testing.

## Development Commands

```bash
pip install -e ".[dev]"                      # Install with dev extras
python -c "from smelt.schemas import WorkItem, WorkResult, TaskStatus"  # Verify schemas
docker compose up                            # Start NATS + Redis
```

## What NOT to Do

- Do not add working LLM client code to this repository - it belongs in the private repo
- Do not add Postgres/pgvector/Jaeger to docker-compose.yml - the scaffold uses NATS + Redis only
- Do not create a `src/smelt/llm/` directory - the full LLM client is private
- Do not commit `.env` - only `.env.example` belongs here
- Do not remove or weaken the LICENCE file

## Licence Reminder

This repository is distributed under a proprietary view-only licence. The source is provided
for inspection and evaluation only. See `LICENCE` for exact terms.
