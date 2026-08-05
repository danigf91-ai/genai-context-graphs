"""Module 3 challenge - promote entities to long-term memory. Completed."""

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

SESSION_ID = "graphacademy"

MESSAGE = "I am Alex Mercer and I work at Ridgeline Labs."


async def main():
    async with MemoryClient(settings) as memory:
        # Extraction is on by default, so storing the message is enough to
        # promote the people and organizations it names into long-term memory.
        message = await memory.short_term.add_message(SESSION_ID, "user", MESSAGE)
        print(f"Stored message {message.id}")

        preference = await memory.long_term.add_preference(
            category="communication",
            preference="Prefers concise answers",
            context="Stated in the first conversation",
        )
        print(f"Stored preference {preference.id}")

        print("\nEntities in long-term memory matching 'Alex':")
        entities = await memory.long_term.search_entities(query="Alex", limit=5)
        for entity in entities:
            print(f"  {entity.name} ({entity.entity_type})")


asyncio.run(main())
