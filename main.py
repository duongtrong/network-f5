from service.f5gtm import get_access_token
from service.f5gtm import config_mgmt_f5system
from service.f5gtm import save_sys_config
import urllib3
urllib3.disable_warnings()

username = 'admin'
password = 'Tcb123'
hostname = '47.129.45.25:8443'
deviceId = 'f5test'

def get_access_token_method():
    try:
        get_access_token_result = get_access_token(
            username=username,
            password=password,
            host=hostname)
        if get_access_token_result['status'] == 200:
            token = get_access_token_result['token']
            return {'status': 200, 'token': token}
        else:
            return {'status': 'Bad Request', 'msg': 'ERROR'}
    except Exception as e:
        return {'status': 'Bad Request', 'msg': 'Exception: {}'.format(str(e))}
# end try

if __name__ == "__main__":
    result_token = get_access_token_method()
    print(result_token['token'])
    configF5 = config_mgmt_f5system(username=username, password=password, timezone="Asia/Saigon", host=hostname, device=deviceId)
    print(configF5)
    # state = save_sys_config(token=result_token["token"], host=hostname)
    # print(state)
