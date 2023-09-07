# default object

class sessionfuncs():
    def __init__(self, port=4723, host="localhost"):
        self.port=port
        self.host=host

    def setport(self, port):
        self.port=port

    def sethost(self, host):
        self.host=host

    from ._sessionfuncs import kill_sessions_by_udid, kill_sessions, killall_sessions, is_udid_busy, get_sessions_of_udid, busy_devices, get_sessions_by_desiredcap, get_udid_by_desiredcap
