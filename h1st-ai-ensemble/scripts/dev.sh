#!/bin/bash
./setup.sh

PORT=8001
BASEDIR=$(dirname $0)
echo "Starting local server"

pm2 start ${BASEDIR}/app.json -- --port=$PORT
ngrok http $PORT
