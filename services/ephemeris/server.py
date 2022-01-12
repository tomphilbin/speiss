import asyncio
import grpc
import logging
import os

import satellite_passes
import ephemeris_pb2
import ephemeris_pb2_grpc


class Ephemeris(ephemeris_pb2_grpc.EphemerisServicer):

    async def GetAllSatellitePasses(self, request: ephemeris_pb2.SatellitePassesRequest,
                     context: grpc.aio.ServicerContext) -> ephemeris_pb2.SatellitePassesResponse:

        passes = satellite_passes.calculate(request.tle, request.start_date,
                                            request.end_date, request.location)

        return ephemeris_pb2.SatellitePassesResponse(items=passes)


async def serve() -> None:
    server = grpc.aio.server()
    ephemeris_pb2_grpc.add_SatellitePassesServicer_to_server(
        Ephemeris(), server)
    listen_addr = os.environ.get('LISTEN_ADDR') or '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
