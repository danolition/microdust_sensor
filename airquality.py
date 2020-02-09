import serial, time
from Adafruit_IO import Client
aio = Client('danolition', 'aio_qHfO03cBlDgIMDUmOEfFzS49mCQF')
ser = serial.Serial('/dev/ttyUSB0')
while True:
    data = []
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)
    pmtwofive = int.from_bytes(b''.join(data[2:4]),byteorder='little') / 10
    #we are posting the content of pmtwofive to the feed belfastsouthtwofive that we have created previously
    aio.send('belfastsouthtwofive', pmtwofive)
    pmten = int.from_bytes(b''.join(data[4:6]),byteorder='little') / 10
    #we are posting the content of pmten to the feed belfastsouthten that we have also created before
    aio.send('belfastsouthten', pmten)
    time.sleep(10)

