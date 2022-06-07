import asyncio
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from websockets.server import WebSocketServerProtocol, serve
import random
import sys
import numpy as np

from message_pb2 import MessageData, DataType, DataRequest


def create_random_point(n):
    result = []
    for _ in range(n):
        result.append(random.random() * 12000)
    return result


async def handler(websocket: WebSocketServerProtocol):
    while True:
        try:
            message = await websocket.recv()
            req = DataRequest()
            if isinstance(message, bytes):
                req.ParseFromString(message)
                response = MessageData()
                if req.type == DataType.LRFDATA:
                    response.type = DataType.LRFDATA
                    response.x.extend(create_random_point(720))
                    response.y.extend(create_random_point(720))
                await websocket.send(response.SerializeToString())
            else:
                pass
        except ConnectionClosedOK:
            print("Closed")
            break
        except ConnectionClosedError as e:
            print("Connection Error", e, file=sys.stderr)


async def main():
    async with serve(handler, "localhost", 3334):
        await asyncio.Future()  # run forever


# asyncio.run(main())
loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
