# WXTools

## SN_to_COM.py

### Pulls location from SpotterNetwork and outputs them as GPS NMEA sentences to a COM port

1. ```pip install pyserial requests```
2. Download and install [sourceforge.net/projects/com0com](https://sourceforge.net/projects/com0com/)
3. Enter the following command using the newly installed tool at C:\Program Files (x86)\com0com\setupc.exe
   ```
   install PortName=COM50 PortName=COM51
   ```
   (or use your own ports)
4. Set one of those ports as virt_com_input and use the other in your software (tested on GRLevelX)
5. Get your Application ID from [spotternetwork.org/account](https://www.spotternetwork.org/account) and paste it in sn_app_id
