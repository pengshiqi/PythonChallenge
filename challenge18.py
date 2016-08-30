import gzip
import difflib

file = gzip.open('deltas.gz', 'r')
content = file.readlines()
file.close()
# print content

left, right = [], []

for row in content:
    left.append(row[:53])
    right.append(row[56:])

diff = list(difflib.ndiff(left, right))
# print diff
print 'diff'

png =['', '', '']
for row in diff:
    bytes = [chr(int(byte, 16)) for byte in row[2:].split()]
    if row[0] == '-': png[0]+=''.join(bytes)  
    elif row[0]=='+': png[1]+=''.join(bytes)  
    elif row[0]==' ': png[2]+=''.join(bytes)  

for i in range(3):  
    open('out18_%d.png' %i,'wb').write(png[i])