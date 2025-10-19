#!/bin/bash
echo "1) Insert unique record"
curl -s -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","age":25}' || true
echo -e "\n2) Try exact duplicate"
curl -s -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","age":25}' || true
echo -e "\n3) Try near-duplicate"
curl -s -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john_doe@example.com","age":25}' || true
