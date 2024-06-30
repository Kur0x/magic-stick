from machine import I2C, Pin
from imu import MPU6050
from enhanced_neopixel import EnhancedNeoPixel
import time

# Initialize the I2C bus
i2c = I2C(0, scl=Pin(4), sda=Pin(3), freq=400000)
np = EnhancedNeoPixel(8)

# Initialize MPU6050
# Here '0' or '1' depends on the address pin connection of your MPU6050 module
try:
    mpu = MPU6050(i2c, device_addr=0)
except Exception as e:
    print('Failed to initialize MPU6050:', str(e))
mpu.accel_range = 1
def read_sensor_data():
    """Function to read and print accelerometer and gyroscope data."""
    accel_data = mpu.accel.xyz
    gyro_data = mpu.gyro.xyz
    print('Accelerometer:', accel_data)
    print('Gyroscope:', gyro_data)

# # Main loop to repeatedly read sensor data
# while True:
#     read_sensor_data()
#     time.sleep(1)  # Delay for 1 second

import network
import urequests as requests
import time

def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

def control_homeassistant(entity_id, action):
    url = 'http://10.0.0.222:8123/api/services/light/{}'.format(action)
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyODEwZjM0NWQ5MDE0NjgwYjQ0Y2JhZjljNGRhZTEyMCIsImlhdCI6MTcxOTQ5NTc1MCwiZXhwIjoyMDM0ODU1NzUwfQ.PNm3huPTkvCa5V9PRdG8tnygq-MHY00MGKrs_vCxKMs',
        'Content-Type': 'application/json'
    }
    data = {
        'entity_id': entity_id
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.text)

def main():
    connect_wifi('23A', '05722067')
    while True:
        if mpu.accel.x > 3:
            np.set_color("red", brightness=1)
            control_homeassistant('light.yeelink_ceil38_357e_light', 'toggle')
            time.sleep(1)
            np.clear()
            

main()