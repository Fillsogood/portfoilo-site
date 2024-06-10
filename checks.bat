@echo off

poetry run black .
poetry run isort .
poetry run mypy .
