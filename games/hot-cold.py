import utilities.now as espnow
import utilities.lights as lights
import time, json

class Hot_cold:
    def __init__(self):
        hidden_gem=b'\xf0\xf5\xbd-\x17x'

        def my_callback(msg, mac, rssi):
            if msg == 'ping':
                try:
                    strength = rssi[hidden_gem][0]
                    strength += 30 # best possbile case
                    s = int(12 + 3 * strength/10)
                    max(0, min(s, 11))
                    print(strength)
                    led.show_number(s, lights.RED, 0.1)
                except:
                    pass
            
        led = lights.Lights()
        now = espnow.Now(my_callback)
        now.connect()
        print(now.wifi.config('mac'))

async def main(obj):
    play = Hot_cold()
    task = asyncio.create_task(play.run())
    while obj.running:
        print('@',end='')
        await asyncio.sleep(1)
    print('ending hot cold game')
    play.running = False
    await task
