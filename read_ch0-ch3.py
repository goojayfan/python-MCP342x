#!/usr/bin/env python3
import glob
import smbus
from MCP342x import MCP342x
import numpy as np

addr = 0x68


def get_smbus():
    candidates = []
    prefix = '/dev/i2c-'
    for bus in glob.glob(prefix + '*'):
        try:
            n = int(bus.replace(prefix, ''))
            candidates.append(n)
        except:
            pass
    if len(candidates) == 1:
        return smbus.SMBus(candidates[0])
    elif len(candidates) == 0:
        raise Exception("Could not find an I2C bus")
    else:
        raise Exception("Multiple I2C busses found")



bus = get_smbus()

# Create objects for each signal to be sampled
# get i2c addr by `sudo i2cdetect -y 1`
addr68_ch0 = MCP342x(bus, addr, channel=0, resolution=18)
addr68_ch1 = MCP342x(bus, 0x68, channel=1, resolution=16)
addr68_ch2 = MCP342x(bus, 0x68, channel=2, resolution=14)
addr68_ch3 = MCP342x(bus, 0x68, channel=3, resolution=12)


# Create a list of all the objects. They will be sampled in this
# order, unless any later objects can be sampled can be moved earlier
# for simultaneous sampling.
adcs = [addr68_ch0, addr68_ch1, addr68_ch2, addr68_ch3]
r = MCP342x.convert_and_read_many(adcs, samples=3)
print('return values: ')
print(r)

