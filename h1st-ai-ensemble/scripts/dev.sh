#!/bin/bash

PORT=8001
BASEDIR=$(dirname $0)

${BASEDIR}/setup.sh

echo "Starting local server"

pm2 start ${BASEDIR}/app.json -- --port=$PORT
ngrok http $PORT
