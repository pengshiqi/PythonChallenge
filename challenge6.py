import re
import zipfile

num = '90052'
comments = []
z = zipfile.ZipFile('channel.zip', 'r')

while (num):
    comments.append(z.getinfo('{0}.txt'.format(num)).comment)
    text = z.read('{0}.txt'.format(num))
    print text
    num = ''.join(re.findall(r'[0-9]', text))

print ''.join(comments)