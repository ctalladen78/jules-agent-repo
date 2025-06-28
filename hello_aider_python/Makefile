# Makefile for hello_aider Python

all: server.py

greeting.py:
    python3 -m compileall greeting.py

run:
    uvicorn main:app --reload

dev:
    uvicorn main:app --reload --host 0.0.0.0:3000

test:
    pytest
