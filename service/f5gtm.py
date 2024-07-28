import requests 
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

def get_access_token(username, password, host):
    """
        Username: username
        Password: password
        Host: host
    """
    url = "https://{}/mgmt/shared/authn/login".format(host)
    
    data = {
        "username": username,
        "password": password,
        "loginProvideName": "tmos" 
    }
    payload = json.dumps(data)
    try:
        response = requests.post(url=url, data=payload, verify=False)
        if response.status_code == 200:
            token = json.loads(response.text)['token']['token']
            return {'status': 200, 'token': token}
        else:
            return {'status': 'Bad Request', 'msg': response.text}
    except Exception as e:
        return {'status': 400, 'msg': str(e)}

def config_mgmt_timeZone(username, password, timezone, host):
    """
        username
        password
        timeZone
        hostname
    """
    url = "https://{}/mgmt/tm/sys/ntp".format(host)
    data = {
        "timezone": timezone
    }
    payload = json.dumps(data)
    try:
        response = requests.put(url=url, auth=(username, password), verify=False, data=payload)
        if response.status_code == 200:
            print("Insert success")
            return {"status": 200, "msg": "Successfully"}
        else:
            print("Insert fail")
            return {"status": 400, "msg": response.text}
    except Exception as e:
        return { "status": 400, "msg": str(e)}

def save_sys_config(token, host):
    """
        token
        hostname
    """
    url = "https://{}/mgmt/tm/sys/config".format(host)
    headers = {"X-F5-Auth-token": token}
    data = {
        "command": "save"
    }
    payload = json.dumps(data)
    try:
        response = requests.post(url=url, headers=headers, verify=False, data=payload)
        if response.status_code == 200:
            print("Insert success")
            return {"status": "OK"}
        else:
            print("Insert fail")
            return {"status": "NOK", "msg": response.text}
    except Exception as e:
        return { "status": 400, "msg": str(e)}