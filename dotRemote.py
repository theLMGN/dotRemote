import logging
import json
import d
import lcd
from lcd import lcd
from backlight import backlight
from config import *
from websocket_server import WebsocketServer

def new_client(client, server):
    allowed = CLIENTAUTH(client["address"][0])
    print("Recieved connection from " + client["address"][0] + ", allowed: " + str(allowed))
    if allowed == True:
        server.send_message(client,json.dumps({'type': "welcome", 'error': False}))
    else:
        server.send_message(client,json.dumps({'type': "forbidden", 'error': True}))

def message(client,server,message):
    allowed = CLIENTAUTH(client["address"][0])
    print("Recieved message from " + client["address"][0] + ", allowed: " + str(allowed))
    try:
        if allowed == True:
            data = json.loads(message)
            if data["module"] == "lcd":
                server.send_message(client,json.dumps({'type': 'response', 'return': lcd(data),'invoker': data}))
            if data["module"] == "backlight":
                server.send_message(client,json.dumps({'type': 'response', 'return': backlight(data),'invoker': data}))
            
        else:
            server.send_message(client,json.dumps({'type': "forbidden", 'error': True}))
    except:
        server.send_message(client,json.dumps({'type': "error", 'error': True}))
        pass
        



server = WebsocketServer(SERVER_PORT, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_recieved(message)
server.run_forever()