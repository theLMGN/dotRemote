from dothat import lcd
def lcd(data):
    if data["command"] == "write":
        lcd.write(data["value"])
        return True
    if data["command"] == "clear":
        lcd.clear()
        return True
    if data["command"] == "set_contrast":
        lcd.set_contrast(data["contrast"])
        return True
    if data["command"] == "set_cursor_position":
        lcd.set_cursor_position(data["column"],data["row"])
        return True
    if data["command"] == "set_cursor_offset":
        lcd.set_cursor_offset(data["offset"])
        return True
    if data["command"] == "set_display_mode":
        lcd.set_display_mode(data["enable"],data["cursor"],data["blink"])
        return True
    if data["command"] == "create_char":
        lcd.create_char(data["char_pos"],data["char_map"])
        return True
    if data["command"] == "create_animation":
        lcd.create_animation(data["anim_pos"],data["anim_map"],data["frame_rate"])
        return True
    if data["command"] == "update_animations":
        lcd.update_animations()
        return True