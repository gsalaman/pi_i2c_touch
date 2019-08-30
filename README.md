# pi_i2c_touch
I2c example code for the touch pot

# Installing I2C
First need to enable I2C.  Do a sudo raspi-config, select "interfacing options", and turn on I2C.  (doc said it was under advanced...if it's not under interfacing, check there)

Next, need the python libraries.  Do "sudo apt-get install python-smbus i2c-tools". 

Then "sudo reboot" to make the pins available.

(note:  matrix is still available at this point.)

# command line test
Connect up your i2c device, and run:  
sudo i2cdetect -y 1  

That should list out the addresses that i2c device uses.

bus 1 uses pins 3 and 5 for SDA and SCL


