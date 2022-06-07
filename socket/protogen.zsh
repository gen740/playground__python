#!/bin/zsh

protoc --python_out=. --mypy_out=. ./message.proto
