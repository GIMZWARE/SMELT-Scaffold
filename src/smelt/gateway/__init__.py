"""SMELT gateway — FastAPI ingress with validation and trace stamping.

This module is a stub. The full implementation (available at smelt.gimzware.ai)
contains:

  FastAPI application (app)
    POST /tasks — accepts TaskRequest, validates payload_json against the
    agent_type's payload schema, stamps a trace_id (UUID v4), and publishes
    a WorkItem to the orchestrator via NATS.
    GET /tasks/{task_id} — returns current TaskState from Postgres memory.
    GET /health — liveness and readiness probes.

  Middleware
    OpenTelemetry FastAPI instrumentation for automatic span creation per request.
    Structured request/response logging with trace ID correlation.

  Lifespan
    Async context manager for startup (NATS connect, DB pool init) and
    shutdown (NATS drain, DB pool close) without blocking the event loop.

Implement the FastAPI app and lifespan in this package to replace these stubs.
"""
