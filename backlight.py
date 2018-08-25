from dothat import backlight
from config import USE_RBG
if USE_RBG:
    backlight.use_rbg()

def backlight(data):
    if data["command"] == "off":
        backlight.off()
        return True
    
    if data["command"] == "sweep":
        backlight.sweep(data["hue"],data["range"])
        return True

    if data["command"] == "hue":
        backlight.hue(data["hue"])
        return True
    if data["command"] == "rgb":
        backlight.rgb(data["r"],data["g"],data["b"])
        return True

    if data["command"] == "left_hue":
        backlight.left_hue(data["hue"])
        return True
    if data["command"] == "left_rgb":
        backlight.left_rgb(data["r"],data["g"],data["b"])
        return True

    if data["command"] == "mid_hue":
        backlight.mid_hue(data["hue"])
        return True
    if data["command"] == "mid_rgb":
        backlight.mid_rgb(data["r"],data["g"],data["b"])
        return True

    if data["command"] == "right_hue":
        backlight.right_hue(data["hue"])
        return True
    if data["command"] == "right_rgb":
        backlight.right_rgb(data["r"],data["g"],data["b"])
        return True

    if data["command"] == "set":
        backlight.set(data["index"],data["value"])
        return True

    if data["command"] == "set_bar":
        backlight.set_bar(data["index"],data["value"])
        return True
    if data["command"] == "set_graph":
        backlight.set(data["value"])
        return True

    if data["command"] == "update":
        backlight.update()
        return True