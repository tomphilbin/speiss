python3 -m grpc_tools.protoc -I ./services/protos --python_out=./services/satellite-passes --grpc_python_out=./services/satellite-passes ./services/protos/satellite_passes.proto