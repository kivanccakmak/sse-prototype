#!/bin/bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"foo": "bar"}' \
http://127.0.0.1:5001/sio_hello
