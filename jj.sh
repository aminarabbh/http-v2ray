#!/bin/sh
python3 config.py
cat config.json
./v2ray -config=config.json
