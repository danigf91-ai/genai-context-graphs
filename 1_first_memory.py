"""Module 1 challenge - store your first memory.

Complete the TODOs, then run:  python 1_first_memory.py
"""

import asyncio
import os

from dotenv import load_dotenv
from neo4j_agent_memory import ExtractionConfig, MemoryClient, MemorySettings
from neo4j_agent_memory.config import Neo4jConfig

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

# Every challenge in this course writes to the same session.
SESSION_ID = "graphacademy"


async def main():
    async with MemoryClient(settings) as memory:
        message = await memory.short_term.add_message(
            SESSION_ID, "user", "I am learning Neo4j and GraphRAG."
        )
        print(f"Stored message {message.id} in session {SESSION_ID}")

asyncio.run(main())
