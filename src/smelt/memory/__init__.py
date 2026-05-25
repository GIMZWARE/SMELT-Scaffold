"""SMELT memory layer - working memory (Redis) and episodic memory (Postgres).

This module is a stub. The full implementation (available at smelt.gimzware.ai)
contains:

  RedisMemory
    Asyncio client wrapping redis-py for working memory operations.
    Stores transient agent context, task routing hints, and rate-limit counters.
    TTL-based expiry for all keys. No persistent state.

  PostgresMemory
    Asyncio SQLAlchemy + asyncpg client for episodic memory.
    Persists TaskState records with full audit history of status transitions.
    Supports read-by-task-id and time-range queries for observability.
    Schema managed via Alembic migrations.

  VectorMemory (optional, requires pgvector extension)
    Semantic retrieval layer backed by pgvector.
    Stores agent output embeddings for RAG retrieval in subsequent tasks.
    Requires the [embeddings] optional dependency group.

Implement RedisMemory and PostgresMemory in this package to replace these stubs.
"""
