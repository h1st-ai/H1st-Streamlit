#!/bin/bash

BASEDIR=$(dirname $0)
echo "Script location: ${BASEDIR}"

pip install -r ${BASEDIR}/../app/api/requirements.txt
pip install -r ${BASEDIR}/../app/ai/requirements.txt