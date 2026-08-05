#!/usr/bin/env bash
set -e

pip install --upgrade pip
pip install -r requirements.txt

# Give the learner a .env to fill in, and open it so the next step is obvious.
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example - fill in the values from the course."
fi
