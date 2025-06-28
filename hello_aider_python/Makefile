# Makefile for hello_aider Python

all: greeting.py

greeting.py:
    python3 -m compileall greeting.py

run:
    uvicorn main:app --reload

dev:
    uvicorn main:app --reload --host 0.0.0.0

test:
    pytest
