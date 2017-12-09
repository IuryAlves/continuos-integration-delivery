#!/usr/bin/env bash

set -e


VENV_NAME=continuous_integration_delivery
virtualenv $VENV_NAME --python=python3
source $VENV_NAME/bin/activate

pip install -r requirements.txt

coverage run manage.py test
coverage xml