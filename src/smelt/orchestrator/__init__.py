"""SMELT orchestrator — task lifecycle management over NATS JetStream.

This module is a stub. The full implementation (available at smelt.gimzware.ai)
contains:

  Orchestrator
    Consumes TaskRequest messages from the gateway via NATS.
    Manages full task state transitions (pending -> dispatched -> in_progress
    -> completed/failed/cancelled) with configurable retry logic (MAX_RETRIES=5).
    Writes TaskState records to Postgres episodic memory after each transition.
    Publishes WorkItem messages to per-agent NATS subjects
    (smelt.agents.research, smelt.agents.reasoning, smelt.agents.action).
    Subscribes to smelt.results.* to receive WorkResult messages and finalise tasks.

  OrchestratorConfig
    Dataclass loaded from environment variables. Controls NATS URLs, retry
    budgets, timeout thresholds, and concurrency limits.

  NatsClient
    Thin asyncio wrapper around nats-py JetStream with stream provisioning,
    publish-with-ack, pull consumer management, and graceful drain on shutdown.

Extend this package with your own Orchestrator, OrchestratorConfig, and
NatsClient implementations to replace these stubs.
"""
