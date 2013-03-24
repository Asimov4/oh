import json
import collections
import os
import requests
import time


Auth = collections.namedtuple("AuthCred", ["Token", "Session"])
FileInfo = collections.namedtuple("FileInfo", ["Token", "FileId"])


class EmotionFile:
    def __init__(self, file_name):
        self.url = "http://api.simpleemotion.com/v2/"
        self.apikey = "da71c2686c692cb776e4"
        self.token, self.session = login(self.url, self.apikey)
        self.fileid = ""
        self.file_name = file_name
        self.file_path = str(os.path.abspath(file_name))


def login(url, apikey):
    data = [
        ('command', 'api-login'),
        ('apikey', apikey)
    ]
    auth_json = requests.get(url, params=data)
    j = auth_json.json()
    token = j['token']
    session = j['session']

    return Auth(Token=token, Session=session)


def files_list(ef):
    data = [
        ('command', 'files-list'),
        ('apikey', ef.apikey),
        ('session', ef.session),
        ('token', ef.token)
    ]
    files_json = requests.get(ef.url, params=data)
    j = files_json.json()
    ef.token = j['token']

    return j['files']


def add_file(ef):
    data = [
        ('command', 'add-file'),
        ('apikey', ef.apikey),
        ('session', ef.session),
        ('token', ef.token),
        ('name', ef.file_name),
        ('target', '')
    ]
    add_file = requests.get(ef.url, params=data)
    j = add_file.json()
    ef.token = j['token']
    ef.fileid = j['file']['id']

    return FileInfo(Token=j['token'], FileId=j['file']['id'])


def analyze_file(ef):
    data = [
        ('command', 'analyze-file'),
        ('apikey', ef.apikey),
        ('session', ef.session),
        ('token', ef.token),
        ('fileid', str(ef.fileid))
    ]
    files = {'file': open(ef.file_path, 'rb')}
    analyze_file = requests.post(ef.url, params=data, files=files)
    j = analyze_file.json()
    ef.token = j['token']
    return j


def get_file(ef):
    data = [
        ('command', 'alerts'),
        ('apikey', ef.apikey),
        ('session', ef.session),
        ('token', ef.token),
        ('fileid', str(ef.fileid))
    ]
    get_file = requests.get(ef.url, params=data)
    j = get_file.json()
    return j


def get_alerts(ef):
    data = {
        'command': 'alerts',
        'apikey': ef.apikey,
        'session': ef.session,
        'token': ef.token,
    }
    get_alerts = requests.get(ef.url, params=data)
    j = get_alerts.json()
    return j['alerts']


def receive_alert(ef, alert_id):
    data = {
        'command': 'alert-received',
        'apikey': ef.apikey,
        'session': ef.session,
        'token': ef.token,
        'alertid': alert_id
    }
    receive_alert = requests.get(ef.url, params=data)
    j = receive_alert.json()
    ef.token = j['token']
    return j


def pretty_json(pjs):
    print json.dumps(
        pjs, sort_keys=True, indent=4, separators=(',', ': ')
    )


def predict_file(file_name):
    ef = EmotionFile(file_name)

    print "Adding file"
    add_file(ef)

    print "Submitting and analyzing file"
    analyze_file(ef)

    d = get_alerts(ef)

    for a in d:
        receive_alert(ef, a.get('id', 0))
        if 'ERROR' in a['message']:
            print "ERROR:"
            pretty_json(a)
            break

    last = files_list(ef)[-1]
    while 'analyzing' == last['predicted']:
        time.sleep(0.25)
        last = files_list(ef)[-1]
        if 'ERROR' in last['predicted']:
            print "ERROR:"
            break

    # pretty_json(last)
    return last
