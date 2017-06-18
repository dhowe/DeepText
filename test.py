#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#ax.plot([1,2,3])
#plt.show()


DATA_DIR = 'data/test.txt';

print DATA_DIR
print "hello"

data = open(DATA_DIR, 'r').read()
chars = list(set(data))
VOCAB_SIZE = len(chars)

print chars
print VOCAB_SIZE
