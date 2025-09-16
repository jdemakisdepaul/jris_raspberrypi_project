import time, os 
import requests

MAX_TEMP = 37.0
MIN_T_BETWEEN_WARNINGS = 60 # Minutes

BASE_URL = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
KEY = 'your_key_here'

def send_notification(temp):
    status = 'Thingtweet: Raspberry Pi getting hot. CPU temp=' + str(temp)
    data = {'api_key' : KEY, 'status' : status}
    response = requests.post(BASE_URL, json=data)
    print(response.status_code)

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return float(cpu_temp)

def cpu_temp():
    cpu_temp = CPUTemperature().temperature
    return cpu_temp
    
while True:
    temp = cpu_temp()
    print("CPU Temp (C): " + str(temp))
    if temp > MAX_TEMP:
        print("CPU TOO HOT!")
        send_notification(temp)
        print("No more notifications for: " + str(MIN_T_BETWEEN_WARNINGS) + " mins")
        time.sleep(MIN_T_BETWEEN_WARNINGS * 60)
    time.sleep(1)

