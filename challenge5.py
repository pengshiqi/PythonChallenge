import pickle

file = open('challenge5.txt')

data = pickle.load(file)

for item in data:  
    print "".join(map(lambda p: p[0]*p[1], item))

