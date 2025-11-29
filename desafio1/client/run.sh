#!/bin/sh
while true; do
  curl http://servidor:8080
  echo "Requisição enviada..."
  sleep 3
done