from machine import Pin,ADC
from dht import DHT11
import time
import network
from umqtt.simple import MQTTClient

wifi_ssid = 'Redmi 8'
wifi_pass = 'chancellor66'

aio_username = 'douglasaubre51'
aio_key = 'aio_LXJL08m7kSug5sBWLgv5p8CvfpC9'
aio_broker = 'io.adafruit.com'

aio_gas_topic = f'{aio_username}/feeds/gas_sensor'
aio_pir_topic = f'{aio_username}/feeds/pir_sensor'
aio_temp_topic = f'{aio_username}/feeds/temp_sensor'
aio_humid_topic = f'{aio_username}/feeds/humid_sensor'
aio_gas_topic = f'{aio_username}/feeds/gas_sensor'

buzz = Pin(16, Pin.OUT)

pir = Pin(14, Pin.IN)
gas = ADC(26)
dht_sensor = DHT11(Pin(15,Pin.OUT,Pin.PULL_UP))
dht_sensor.measure()

time.sleep(1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_pass)

while not wlan.isconnected():
    pass

client = MQTTClient(
    aio_username,
    aio_broker,
    user = aio_username,
    password = aio_key)
client.connect()

while True:
    dht_sensor.measure()
    client.publish(aio_temp_topic,str(dht_sensor.temperature()))
    client.publish(aio_humid_topic,str(dht_sensor.humidity()))
    client.publish(aio_pir_topic,str(pir.value()))
    client.publish(aio_gas_topic,str(gas.read_u16()))
    
    print(f'humidity: {dht_sensor.humidity()}')
    print(f'temperature: {dht_sensor.temperature()}')
    
    if(gas.read_u16() >= 14700):
        print(f'SMOKE OR HARMFUL GASES DETECTED!!! CHECK FOR FIRES OR UNCONTROLLED CHEMICAL REACTIONS!!!')
        print(f'mq2_value: {float(gas.read_u16())}')
    else:
        print('AIR QUALITY IS OK')
        print(f'mq2_value: {float(gas.read_u16())}')
    
    print('pir value: ', pir.value())
    if(pir.value() == 0):
        print(f'MOTION DETECTED!!! MIGHT BE A PERSONNEL!!! PROCEED WITH CAUTION!!!')
        print(f'ALARM TRIGGERED!!!')
        buzz.high()
        time.sleep(.3)
        buzz.low()
    else:
        print('MOTION SENSORS ARE WORKING....')
    
    time.sleep(5)