# dotRemote

Remote library for controlling [Pimoroni Display-O-Tron](https://shop.pimoroni.com/products/display-o-tron-hat) HATs remotly using websockets!

### Why?

 - Data only accessible from a device that isn't your Pi
 - Easier debugging/development, using a full IDE/Text editor, and your favorite debugger, keyboard, and whatever you use to code!
 - More language support

## How do I use it?

#### Connection
Connect using websockets to your Pi's IP adress and the port specified in config.py

On connection from a **local** IP address (this can be changed in the config.py, though I wouldn't recommend it) you should see a message like this

```json
    {"type": "welcome", "error": false}
```

Or, if you're not connecting from a local IP address

```json
    {"type": "forbidden", "error": true}
```
#### Sending commands

The general command structure is as follows:

```json
    {"module": "{module}", "command": "{command}"}
```

Additional arguments may be added as necessary 

You could also add your own internal arguments and they will sent back to you (see below)

An example is as follows:

```json
    {"module": "lcd", "command": "set_contrast", "contrast": 30}
```

This would correspond to
```py
lcd.set_contrast(30)
```
as shown as in the [DotHat documentation](https://github.com/pimoroni/displayotron/blob/master/documentation/REFERENCE.md#methods)

We try to maintain the method names and arguments names as in the [docs](https://github.com/pimoroni/displayotron/blob/master/documentation/REFERENCE.md). Check lcd.py or backlight.py if you're stuck.

#### Recieving messages

The general return structure is as follows

```json
    {"type": "response", "return": {return value},"invoker": {the message you sent that corresponded to this action.}}
```

