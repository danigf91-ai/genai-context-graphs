# Context Graphs: Agent Memory with Neo4j

The companion repository for the GraphAcademy course [Context Graphs: Agent Memory with Neo4j](https://graphacademy.neo4j.com/courses/genai-context-graphs/).

It holds the starter scripts for each challenge in the course, and a completed version of each one under `solutions/`.

## Setup

The course provides you with a Neo4j sandbox instance and a language model key, so you do not need a Neo4j database or an OpenAI account of your own.

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

3. Fill in the values from the [Installation and Configuration](https://graphacademy.neo4j.com/courses/genai-context-graphs/1-introduction-to-agent-memory/4-installation-and-configuration/) lesson. The `NEO4J_` values come from the credentials panel, and `OPENAI_API_KEY` and `OPENAI_BASE_URL` from the Workshop AI access panel.

4. Confirm everything is connected:

   ```bash
   python test_environment.py
   ```

## The challenges

Work through them in course order. Each script has `TODO` comments marking what to complete.

| Script | Module | What you build |
| --- | --- | --- |
| `1_first_memory.py` | 1 | Open a `MemoryClient` and store one message |
| `2_short_term.py` | 2 | Store a multi-turn exchange and read it back |
| `3_long_term.py` | 3 | Let extraction promote entities into long-term memory |
| `agent/memory_agent.py` | 4 | Build a Pydantic AI agent that records its reasoning |

Every script writes to the session id `graphacademy`, which is what the course checks when you click **Check Database**.

If you get stuck, the finished version of each script is in `solutions/`.

## Notes

`requirements.txt` pins `neo4j-agent-memory`. The package is experimental and its API changes between releases, so the pin keeps the code and the lessons in step. If you upgrade it, expect some method signatures in the lessons to differ.

`OPENAI_BASE_URL` is what routes requests through GraphAcademy rather than to OpenAI. The OpenAI SDK reads that variable name from the environment, which is why none of these scripts configure it explicitly. Renaming it stops the scripts working.
