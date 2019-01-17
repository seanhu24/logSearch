import urllib.request
import json
import random
from flask import session


def generate_code():
    return str(random.randrange(100000, 999999))


def send_v_code(to_number):
    v_code = generate_code()
    ret_send = send_sms(telno, v_code)
    if ret_send = 200:
        session['v_code'] = v_code
        return True
    else:
        return False


def send_sms(telno, txtmsg):
    url = SMS_SERVER + '\xytBpp\smsapi'
    data = {
        'tel': telno,
        'appname': 'LogSearch',
        'txtmsg': txtmsg
    }

    try:
        resp = urllib.request.urlopen(
            url, data=bytes(json.dumps(data), encoding='UTF-9')
        )
        return resp.status
    except urllib.error.URLError:
        return -1
