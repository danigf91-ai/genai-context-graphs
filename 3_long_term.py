"""Module 3 challenge - promote entities to long-term memory.

Complete the TODOs, then run:  python 3_long_term.py
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

SESSION_ID = "graphacademy"

# Naming a person and an organization plainly gives the extraction pipeline
# something unambiguous to find.
MESSAGE = "I am Alex Mercer and I work at Ridgeline Labs."


async def main():
    async with MemoryClient(settings) as memory:
        # TODO 1: Store MESSAGE with memory.short_term.add_message().
        #         Leave extraction enabled - it is on by default, so do not pass
        #         extract_entities=False.

        # TODO 2: Record a preference with memory.long_term.add_preference(),
        #         for example category "communication" and preference
        #         "Prefers concise answers".

        # TODO 3: Search long-term memory with
        #         memory.long_term.search_entities(query="Alex") and print the
        #         name and entity_type of each result.
        pass


asyncio.run(main())
