#!/usr/bin/env bash
export FLASK_APP=app.py
source $(pipenv --venv)/bin/activate
flask run