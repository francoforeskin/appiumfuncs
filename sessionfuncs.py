# appiumfuncs
# be careful, default port is 10071
import json, requests


def kill_sessions_by_udid(udid, port=10071, host="localhost"):
    session_list=get_sessions_of_udid(udid=udid, port=port, host=host)
    kill_sessions(session_list=session_list, port=port, host=host)


def kill_sessions(session_list, port=10071, host="localhost"):
    for session in session_list:
        requests.delete("http://" + host + ":" + str(port) + "/session/" + session)


def killall_sessions(port=10071, host="localhost"):
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)

    for n in range(len(json_data["value"])):
        requests.delete("http://" + host + ":" + str(port) + "/session/" + json_data["value"][n]["id"])


def is_udid_busy(udid, port=10071, host="localhost"):
    device_list = busy_devices(port=port, host=host)
    return udid in device_list


def get_sessions_of_udid(udid, port=10071, desiredcap="udid", host="localhost"):
    resp = requests.get("http://" + host + ":" + str(port) + "/sessions/")
    json_data = json.loads(resp.text)
    session_list = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["desired"][desiredcap] == udid:
            session_list.append(json_data["value"][n]["id"])

    return session_list


def busy_devices(port=10071, desiredcap="udid", host="localhost"):
    resp = requests.get('http://' + host + ':' + str(port) + '/sessions/')
    json_data = json.loads(resp.text)
    device_list = []

    for n in range(len(json_data["value"])):
        device_list.append(json_data["value"][n]["capabilities"]["desired"][desiredcap])

    return device_list


def get_udid_of_sessions(session_list, port=10071, desiredcap="udid", host="localhost"):
    udid_list = []

    for session_id in session_list:
        resp = requests.get("http://" + host + ":" + str(port) + "/session/" + session_id)
        json_data = json.loads(resp.text)
        udid_list.append(json_data["value"]["desired"][desiredcap])

    return udid_list
