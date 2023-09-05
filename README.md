# Appium Functions I use to do sh*t sending requests
I made those little functions in order to regulate better appium scripts who goes in conflict cause they wanna use the same device.
Having a suite of appium scripts that operate on multiple devices, sometimes simultaneusly on the same device, instead of relying on something pervert like signal handlers or databases I made this tiny lib.

It basically works with lists: lists of sessions, lists of devices...

This readme is basically longer than the code itself

**WARNING** -- THE DEFAULT PORT IS NOT 4723 BUT 10071, CHANGE IT BY SUPPLYING IT TO THE FUNCTIONS

![U professor](https://github.com/francoforeskin/appiumfuncs/blob/master/prof.jpg)
## Requirements
- **requests**
# how to use it
## import every function
```python
from sessionfuncs import *
```
## kill sessions
```python
# kill all sessions using a device
kill_sessions_by_udid(udid="SERIAL CODE OF UR DEVICE", port=4723) # port specified as integer

# get sessions inside a list
MyDevicesSessions = get_sessions_of_udid(udid="SERIAL CODE", port=4723)
# example: kill a list of sessions
kill_sessions(session_list=MyDevicesSessions)

# get_sessions_of_udid is tricky, it uses udid by default but you can specify whatever desired capability you want
AndroidSessions = get_sessions_of_udid(udid="Android", desired_cap="PlatformName", port=4723)
kill_sessions(session_list=AndroidSessions, port=4723) # Kill any android session

# Very useful if you set some "custom" capabilities, this hack is provided by zio Franco
sessions_of_uploading_device = get_sessions_of_udid(udid="upload", desired_cap="custom:activity", port=4723)
```
## check if device is busy
```python
# check if device is currently used by Appium
isBusy = is_udid_busy(udid="SERIAL CODE", port=4723)
if isBusy:
	print("Busy :(")
else:
	print("Device is not used by any sessions")

# get a list of the devices being used by appium
BusyDevices = busy_devices(port=4723)
for Device in BusyDevices:
	print("The device " + Device + " is busy right now :(")
```
