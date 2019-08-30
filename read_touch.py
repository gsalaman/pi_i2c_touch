import smbus
import time

# using channel 1...pins 3 and 5
PI_I2C_CHANNEL = 1

# i2c touchpot address 
TOUCHPOT_ADDR = 9

TOUCHPOT_READ_CMD = 0x47 

bus = smbus.SMBus(PI_I2C_CHANNEL)

while True:
  # give touchpot  a read command
  bus.write_byte(TOUCHPOT_ADDR, TOUCHPOT_READ_CMD)

  # ...and read in the data.
  val = bus.read_byte(TOUCHPOT_ADDR) 
  print(val)

  time.sleep(.5)
