import requests
import re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '12345'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

for i in xrange(400):
    url = base_url + num
    r = requests.get(url, headers=headers)
    num = ''.join(re.findall(r'[0-9]', r.text))
    print num