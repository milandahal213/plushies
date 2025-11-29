## Playground code

Things seem to work.  Move the folder structure down on to a plushie - then replace main.py with the one in games - and then run this code on a different ESP to change the game.

```import utilities.now as espnow
import time, json

def my_callback(msg, mac, rssi):
    print(mac, msg, rssi)
    n.publish(msg, mac)

n = espnow.Now(my_callback)
n.connect()
print(n.wifi.config('mac'))

test = json.dumps({'topic':'/game', 'value':1})
stop = json.dumps({'topic':'/game', 'value':-1})

n.publish(test)
```
