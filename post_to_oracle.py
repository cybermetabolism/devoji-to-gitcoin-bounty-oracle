import emoji
from emoji.unicode_codes import UNICODE_EMOJI
import requests


s = u'\U0001f600'
print("posting message: ", emoji.emojize(UNICODE_EMOJI[s]))

url = 'http://localhost:5000/post/request'
res = requests.post(url,
                    data=s.encode('utf-8'),
                    headers={'Content-type': 'text/plain; charset=utf-8'})
if res.ok:
    print(res.text)
