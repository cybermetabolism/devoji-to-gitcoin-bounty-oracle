import emoji
import requests

my_string = emoji.emojize(":bug:"
                          ":construction_worker:")
my_string_2 = "asdf"


url = 'http://localhost:5000/post/request'
res = requests.post(url,
                    data=my_string_2.encode('utf-8'),
                    headers={'Content-type': 'text/plain; charset=utf-8'})
if res.ok:
    print(res.text)
