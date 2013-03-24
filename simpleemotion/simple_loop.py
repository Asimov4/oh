import simple_emotion as se
import audio_stuff as aud
import requests
import json


app_url = "http://oh.cloudapp.net/oh/simpleemotion/"


f = open('json_output.json', 'w')


while(True):
    aud.record_current()
    p = se.predict_file('output.wav')
    d = {
        'data': json.dumps(p),
        'session': 1,
        'player': 1
    }
    f.write(json.dumps(p) + '\n')

    se.pretty_json(d)
    # d = json.dumps(d)
    # p.append(se.predict_file('output.wav'))

    r = requests.get(app_url, params=d)
    print r
    # print r.text
    print r.url

f.close()
