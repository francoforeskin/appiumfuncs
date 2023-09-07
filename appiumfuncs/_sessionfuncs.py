import json, requests
DEFAULT = object()

def kill_sessions_by_udid(self, udid, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    session_list = self.get_sessions_of_udid(udid=udid, port=port, host=host)
    self.kill_sessions(session_list=session_list, port=port, host=host)


def kill_sessions(self, session_list, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    for session in session_list:
        requests.delete("http://" + host + ":" + str(port) + "/session/" + session)


def killall_sessions(self, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)

    for n in range(len(json_data["value"])):
        requests.delete("http://" + host + ":" + str(port) + "/session/" + json_data["value"][n]["id"])


def is_udid_busy(self, udid, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    device_list = self.busy_devices(port=port, host=host)
    return udid in device_list


def get_sessions_of_udid(self, udid, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)
    session_list = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["deviceUDID"] == udid:
            session_list.append(json_data["value"][n]["id"])

    return session_list


def busy_devices(self, port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    resp = requests.get('http://' + host + ':' + str(port) + '/sessions/')
    json_data = json.loads(resp.text)
    device_list = []

    for n in range(len(json_data["value"])):
        device_list.append(json_data["value"][n]["capabilities"]["deviceUDID"])

    return device_list


def get_sessions_by_desiredcap(self, hostdesiredcap="platformName", matching="Android", port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)
    session_list = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["desired"][desiredcap] == matching:
            session_list.append(json_data["value"][n]["id"])

    return session_list


def get_udid_by_desiredcap(self, desiredcap="platformName", matching="Android", port=DEFAULT, host=DEFAULT):
    if port is DEFAULT:
        port=self.port
    if host is DEFAULT:
        host=self.host
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)
    udid_list = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["desired"][desiredcap] == matching:
            udid_list.append(json_data["value"][n]["id"]["capabilities"]["deviceUDID"])

    return udid_list
