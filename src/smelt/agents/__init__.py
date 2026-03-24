"""SMELT worker agents — autonomous units that process WorkItems.

This module is a stub. The full implementation (available at smelt.gimzware.ai)
contains three concrete agent classes and a shared base:

  BaseAgent (abstract)
    Subscribes to a NATS pull consumer for its agent_type subject.
    Deserialises WorkItem[T] using the agent-specific payload type.
    Calls process() (implemented by each subclass) and publishes a WorkResult
    to smelt.results.<agent_type>.
    Handles retries, error capture, token usage recording, and trace propagation.

  ResearchAgent(BaseAgent)
    Payload: ResearchPayload (query, max_sources, search_web).
    Uses LLMClient with tool_use for web search and RAG retrieval.
    Returns structured citations and summarised findings.

  ReasoningAgent(BaseAgent)
    Payload: ReasoningPayload (prompt, context, voting_rounds).
    Runs N parallel LLM completions (voting_rounds) and applies self-consistency
    voting to select the most coherent answer.

  ActionAgent(BaseAgent)
    Payload: ActionPayload (tool_name, parameters, requires_approval).
    Routes tool calls to registered tool handlers.
    Supports a PendingApproval gate for high-risk actions.

Implement BaseAgent and the three subclasses in this package to replace
these stubs.
"""
