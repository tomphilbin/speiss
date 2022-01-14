#!/bin/bash

python3 -m grpc_tools.protoc \
    -I ./services/protos \
    --python_out=./services/ephemeris \
    --grpc_python_out=./services/ephemeris \
    ./services/protos/ephemeris.proto