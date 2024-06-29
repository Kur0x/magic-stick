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
    # time.sleep(5)
    control_homeassistant('light.yeelink_ceil38_357e_light', 'toggle')


main()