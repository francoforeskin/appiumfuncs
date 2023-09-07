# Appium Functions I use to do sh*t sending requests
I made those little functions in order to regulate better appium scripts who goes in conflict cause they wanna use the same device.
Having a suite of appium scripts that operate on multiple devices, sometimes simultaneusly on the same device, instead of relying on something pervert like signal handlers or databases I made this tiny lib.

![U professor](https://github.com/francoforeskin/appiumfuncs/blob/master/prof.jpg)
## Requirements
- **requests**

## Two classes of *funcs*
### sessionfuncs
### magickfuncs
# how to use this sh*t
## import sessionfuncs
```python
from appiumfuncs import sessionfuncs

sf = sessionfuncs()
```
## kill sessions
```python
# kill all sessions using a device
sf.kill_sessions_by_udid(udid="SERIAL CODE OF UR DEVICE") # port specified as integer

# get sessions inside a list
MyDevicesSessions = get_sessions_of_udid(udid="SERIAL CODE")
# kill a list of sessions
kill_sessions(session_list=MyDevicesSessions)
```
## check if device is busy
```python
# check if device is currently used by Appium
if sf.is_udid_busy(udid="SERIAL CODE"):
	print("Busy :(")
else:
	print("Device is not used by any sessions")
```
## the genius
![Invented the telephone](https://github.com/francoforeskin/appiumfuncs/blob/master/genius.jpg)
```python
# set custom capabilities and manage the device with it.
# Too lazy to show you how, figure it out by yourself.
```
