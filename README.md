# Appium Functions
## sessionfuncs
DEFAULT PORT IS 10071, THAT'S WHAT I USE USUALLY, CHANGE IT BY SUPPLYING TO THE FUNCTIONS
I made those little functions in order to regulate better appium scripts who goes in conflict cause they wanna use the same device.
Having a suite of appium scripts that operate on multiple devices, sometimes simultaneusly on the same device, instead of relying on something pervert like signal handlers or databases I made this tiny lib.
## elfuncs
Those functions works with elements, they do sorting by coordinates and there's a tesseract implementation for finding text inside elements who doesn't have text specified within attributes

![U professor](https://github.com/francoforeskin/appiumfuncs/blob/master/prof.jpg)
## Requirements
### sessionfuncs
- **requests**
### elfuncs
- install tesseract-ocr on your system
- **pytesseract**

# sessionfuncs
## import sessionfuncs
```python
from appiumfuncs import sessionfuncs as sf
```
## kill sessions
```python
# kill all sessions using a device
sf.kill_sessions_by_udid(udid="SERIAL CODE OF UR DEVICE", port=10071) # port specified as integer

# get sessions inside a list
MyDevicesSessions = sf.get_sessions_of_udid(udid="SERIAL CODE")
# kill a list of sessions
sf.kill_sessions(session_list=MyDevicesSessions)
```
## check if device is busy
```python
# check if device is currently used by Appium
if sf.is_udid_busy(udid="SERIAL CODE"):
	print("Busy :(")
else:
	print("Device is not used by any sessions")
```
## a little trick
```python
# set custom capabilities and manage the device with it.
# Too lazy to show you how, figure it out by yourself.
```
# elfuncs
## import elfuncs
```python
from appiumfuncs import elfuncs as ef
```
## examples
```python
# nonsense example
elements = find_elements( ... )
ef.sort_elements_from_bottom(elements)

for el in elements:
	print(element_text_tesseract(el))
```
