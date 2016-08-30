# method 1

# import re

# st = '1'

# pattern = re.compile(r'((?P<w>\d)(?P=w)*)')

# for i in xrange(30):
#     a = map(lambda x: '%s%s'%(len(x[0]), x[1]), pattern.findall(st))
#     st = ''.join(a)

# print len(st)

# method 2

st = '1'

for i in xrange(30):
    temp = 0
    ch = st[temp]
    count = 1
    new_st = ''
    while temp <= len(st):
        temp += 1
        if temp < len(st):
            if ch == st[temp]:
               count += 1
            else:
                new_st += ch + str(count)
                ch = st[temp]
                count = 1
    new_st += ch + str(count)
    st = new_st
    print st

print len(st)
