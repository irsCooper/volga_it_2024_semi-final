SHELL := /bin/bash
.PHONY:
.SILENT:


install:
	# python3 -m venv .venv
	# . .venv/bin/activate && 
	pip install -r requirements.txt


venv:
	. .venv/bin/activate


run:
	uvicorn src.main:app --reload