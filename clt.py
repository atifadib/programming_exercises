
outcomes = [1,2,3,4,5,6]

import numpy as np

def pick():
    return np.random.choice(range(1,7),p=[0.2,0.2,0.1,0.1,0.2,0.2])

p=[0.2,0.2,0.1,0.1,0.2,0.2]
x = [_ for _ in range(1,7)]
prod = 0
for i,j in zip(p,x):
    prod += i*j
mean = prod
print("Mean: ",mean)

distribution = [pick() for _ in range(10000)]

import matplotlib
import matplotlib.pyplot as plt

c = dict()
for _ in distribution:
    try:
        c[_]+=1
    except KeyError:
        c[_]=1

c = sorted([(k,v) for k,v in c.items()],key=lambda x:x[0])
print(c)

#plt.plot([i[0] for i in c],[i[1] for i in c])
#plt.fill_between([i[0] for i in c],[i[1] for i in c])
#plt.xlabel("Outcome")
#plt.ylabel("Freq")
#plt.show()

from random import randint

def random_sample(size=4):
    sample = []
    for _ in range(size):
        sample.append(randint(1,6))
    return sample

import matplotlib.animation as animation
#import matplotlib.pyplot as plt
print(matplotlib.get_backend())
from tqdm import tqdm
samples = []
size = 40
plots = []
#fig = plt.gcf()
#fig.show()
#fig.canvas.draw()

means = 0
dist = {}
#plt.show()
for _ in range(10000):
#    print(_)
    plt.clf()
    sample = random_sample(size)
    new_mean = sum(sample)/size
    means+=new_mean
    running_mean = means/(_+1)
    if new_mean in dist.keys():
        dist[new_mean]+=1
    else:
        dist[new_mean]=1
    pp = sorted([(k,v) for k,v in dist.items()],key=lambda x:x[0])
    plt.title("Iteration:"+str(_)+" Mean:"+str(mean)+" Running Mean:"+str(running_mean))
    plt.plot([i[0] for i in pp],[i[1] for i in pp],color='b')
    plt.fill_between([i[0] for i in pp],[i[1] for i in pp])
    #fig.canvas.draw()
    plt.draw()
    plt.pause(0.001)
plt.ioff()
plt.show()
