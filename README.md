# MCP342x
A Python module to support Microchip MCP342x analogue to digital converters. The devices use the I2C bus. For the low level I2C protocol this module depends on SMBus.

## Supported devices
+ MCP3422: 2 channel, 12, 14, 16, or 18 bit
+ MCP3423: 2 channel, 12, 14, 16, or 18 bit
+ MCP3424: 4 channel, 12, 14, 16, or 18 bit
+ MCP3426: 2 channel, 12, 14, or 16 bit
+ MCP3427: 2 channel, 12, 14, or 16 bit
+ MCP3428: 4 channel, 12, 14, or 16 bit
The MCP3422 and MCP3426 use I2C address 0x68, all other devices can be configured to use any address in the range 0x68 - 0x6F (inclusive).


## 简介
MCP3422/3/4 系列ADC模块具有很高的测量精度，要使其在树莓派上正常工作，需要使用相应的程序/脚本调用。
python3-MCP342x在 `https://github.com/stevemarple/python-MCP342x` 的基础上改写，适用于装有python3的树莓派
在树莓派上运行:
```
sudo apt install build-essential libi2c-dev i2c-tools python-dev libffi-dev
```
之后把 `MCP342x.py` 复制到项目文件夹下即可
使用 `sudo i2cdetect -y 1` 查看 MCP342x 的地址， 然后对脚本进行相应修改即可


## 参考
+ http://www.microchip.com/wwwproducts/en/en536354
+ [中文] http://www.dfrobot.com.cn/images/upload/File/201409251650460rc3v2.pdf

