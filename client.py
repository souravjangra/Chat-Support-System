import asyncio
from contextlib import suppress
import websockets

async def client(url: str):
	async with websockets.connect(url) as websocket:
		while True:
			try:
				message = input("user:>> ")
				await websocket.send(message)
				response = await websocket.recv()
				print(response)
				websocket.send(now)

			except Exception as e:
				# print('Reconnecting')
				websocket = await websockets.connect(url)
			

with suppress(KeyboardInterrupt):
	asyncio.run(client("ws://localhost:8000/conversation"))