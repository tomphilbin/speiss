import asyncio
import grpc
import logging

import calculate_passes
import satellite_passes_pb2
import satellite_passes_pb2_grpc


class SatellitePasses(satellite_passes_pb2_grpc.SatellitePassesServicer):

    async def GetAll(self, request: satellite_passes_pb2.SatellitePassesRequest,
                     context: grpc.aio.ServicerContext) -> satellite_passes_pb2.SatellitePassesResponse:

        passes = calculate_passes.get_all(request.tle, request.start_date,
                                          request.end_date, request.location)

        return satellite_passes_pb2.SatellitePassesResponse(items=passes)


async def serve() -> None:
    server = grpc.aio.server()
    satellite_passes_pb2_grpc.add_SatellitePassesServicer_to_server(
        SatellitePasses(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
