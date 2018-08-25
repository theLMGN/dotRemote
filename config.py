# WS Server port
SERVER_PORT = 3000

# Applies to the Dot3k only. Changes the backlight driver to RBG mode ( instead of RGB ) for early Display-o-Tron boards with reversed B/G channels. Call once after importing dot3k.backlight.
USE_RBG = False 

# Function will be called with the IP every time a message is recieved, if returns true, request will be honoured
def CLIENTAUTH(ip):
    if ip.startswith("127.0.0."):
        return True
    if ip.startswith("192.168."):
        return True
    if ip.startswith("10.0."): 
        return True
    if ip == "localhost":
        return True
    return False
    