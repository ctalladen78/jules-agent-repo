# Makefile for hello_aider Python

.PHONY: all install run dev test clean

all: install run

install:
	pip install -r requirements.txt

run:
	streamlit run streamlit_app.py

dev:
	streamlit run streamlit_app.py --server.port 3000

test:
	pytest

clean:
	rm -rf __pycache__ *.pyc
