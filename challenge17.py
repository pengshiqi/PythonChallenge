import requests
import re
import bz2
import urllib
import xmlrpclib

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
num = '44827'
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
info = ['B']

# while num:
#     url = base_url + num
#     r = requests.get(url, headers=headers)
#     num = ''.join(re.findall(r'[0-9]', r.text))
#     print r.text
#     info.append(r.cookies['info']) 

# print ''.join(info)
st = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

print bz2.decompress(urllib.unquote_plus(st)) # unquote_plus -> decode

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Leopold')


url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
r2 = requests.get(url, headers={'Cookie': 'info=' + urllib.quote_plus('the flowers are on their way')})

print r2.text