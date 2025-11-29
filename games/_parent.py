import time
import asyncio

from utilities.utilities import *
from utilities.lights import *
from utilities.now import *

class Stuffie:
    def __init__(self):
        self.run = False
        self.mac = None
        self.espnow = None
        
    def now_callback(self, msg, mac, rssi):
        print(mac, msg, rssi)
        self.espnow.publish(msg, mac)
    
    async def startup(self):
        print('Starting up')
        a = Lights()
        await a.animate(color = GREEN, intensity = 0.1, number = 12, repeat= 1, timeout = 1.0, speed = 0.05)
        
        self.espnow = Now(self.now_callback)
        self.espnow.connect()
        self.mac = self.espnow.wifi.config('mac')

    async def now_loop(self):
        while self.run:
            await asyncio.sleep(0.1)
            
    def close(self):
        if self.espnow: self.espnow.close()
        

    async def main(self):
        try:
            await self.startup()
            await asyncio.sleep(2)
            
        finally:
            print('shutting down')
            self.close()
   
   
me = Stuffie()
        
asyncio.run(me.main())
    
    