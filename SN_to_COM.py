import serial
import requests
import time

# ===========================
sn_app_id = "" # "Application ID" at https://www.spotternetwork.org/account
virt_com_input = "COM51"    # Virtual COM port input (see below)
interval_seconds = 30       # Interval to pull data and output to serial
# ===========================

while True:
    vrtser = serial.Serial(virt_com_input, 4800)
    sn = requests.get("https://www.spotternetwork.org/pro/feed/" + sn_app_id + "/gm.php")
    deglat = int(float(sn.text.split('lat="')[1].split('"')[0]))
    deglon = int(float(sn.text.split('lng="')[1].split('"')[0]))
    minlat = int((float(sn.text.split('lat="')[1].split('"')[0])-deglat)*60000)/1000
    minlon = int((float(sn.text.split('lng="')[1].split('"')[0])-deglon)*-60000)/1000
    deglon = -deglon
    lat = str(deglat)+"0"+str(minlat) if minlat < 10 else str(deglat)+str(minlat)
    lon = "0"+str(deglon) if deglon < 100 else str(deglon)
    lon = lon+"0"+str(minlon) if minlon < 10 else lon+str(minlon)
    vrtser.write(str.encode("$GPRMC,000000,A," + lat + ",N," + lon + ",W,,,,,A\r\n"))
    vrtser.close()
    time.sleep(interval_seconds)

# ==================== Virtual COM Ports ====================
# Recommend using https://sourceforge.net/projects/com0com/
# Open C:\Program Files (x86)\com0com\setupc.exe
# Use the following command for COM50 and COM51:
# install PortName=COM50 PortName=COM51
# Pick one of those to put in virt_com_input
# and the other as your GPS in GRLevelX
# ===========================================================