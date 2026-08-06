#!/bin/env bash

# Create a virtual environment in the current directory
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from pyproject.toml
python3 -m pip install -r requirements.txt