###############################################################
#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import json

# {"id":"to_arduino_gateway"}

# {"command":"set_mode_digital_output","pin":13}	
# {"command":"digital_write","pin":13,"value":0}	
# {"command":"digital_write","pin":13,"value":1}	
# {"command":"digital_write","pin":13,"value":0}

async def hello():
    uri = "ws://localhost:9000"
    async with websockets.connect(uri) as websocket:

        time.sleep(1)
        # name = json.dumps('to_arduino_gateway')
        name = json.dumps({"id":"to_arduino_gateway"})

        await websocket.send(name)
        time.sleep(0.5)

        name = json.dumps({"command":"set_mode_digital_output","pin":13})

        await websocket.send(name)
        time.sleep(0.5)



        for i in range(10) :
            # name = input("What's your name? ")
            # name = json.dumps('to_arduino_gateway')

            # await websocket.send(name)
            # time.sleep(0.5)

        

            name = json.dumps({'command': 'digital_write', 'pin': 13, 'value': 1})

            await websocket.send(name)
            await asyncio.sleep(1) #async -> sync
            # time.sleep(1)

            # name = json.dumps('to_arduino_gateway')

            # await websocket.send(name)
            # time.sleep(0.5)

            #끄기
            name = json.dumps({'command': 'digital_write', 'pin': 13, 'value': 0})

            await websocket.send(name)
            await asyncio.sleep(1)
            # time.sleep(1)

            greeting = await websocket.recv() # 여기서 메세지 receiving 할려고 계속 기다림. for 문이 진행 안됨.
            print(f"< {greeting}")



        
        # print(f"> {name}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())