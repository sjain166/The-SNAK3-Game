import network, esp, gc

gc.collect()
esp.osdebug(None)

ssid='jacksparrow'  #Network Name
password='Password'  #Network Password

station=network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,password)

while station.isconnected()==False:
    pass
print('connection succesful')
print(station.ifconfig())
