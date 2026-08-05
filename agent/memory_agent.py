"""Module 4 challenge - build and run the agent.

Complete the TODOs, then run:  python agent/memory_agent.py
"""

import asyncio
import os

from dotenv import load_dotenv
from neo4j_agent_memory import ExtractionConfig, MemoryClient, MemorySettings
from neo4j_agent_memory.config import Neo4jConfig
from neo4j_agent_memory.integrations.pydantic_ai import (
    create_memory_tools,
    record_agent_trace,
)
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()

settings = MemorySettings(
    neo4j=Neo4jConfig(
        uri=os.environ["NEO4J_URI"],
        username=os.environ["NEO4J_USERNAME"],
        password=os.environ["NEO4J_PASSWORD"],
    ),
    # The extraction pipeline runs spaCy and GLiNER before falling back to the
    # language model. Those two need extra packages (and a GPU-sized download),
    # so this course uses the LLM stage on its own. Without this, every stored
    # message logs two extractor failures before it succeeds.
    extraction=ExtractionConfig(enable_spacy=False, enable_gliner=False),
)

SESSION_ID = "graphacademy"

# Sends the agent's requests through GraphAcademy rather than to OpenAI.
model = OpenAIChatModel(
    "gpt-4o-mini",
    provider=OpenAIProvider(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
    ),
)

PROMPTS = [
    "My name is Alex and I prefer concise answers.",
    "What do you know about me?",
]


async def main():
    # TODO 1: Open a MemoryClient using `async with`

    # TODO 2: Build the memory tools with create_memory_tools(memory) and pass
    #         them to Agent(model, tools=...)

    # TODO 3: For each prompt in PROMPTS, await agent.run(prompt), print
    #         result.output, then call:
    #           await record_agent_trace(
    #               memory.reasoning, SESSION_ID, result, task=prompt
    #           )
    pass


asyncio.run(main())
