import matplotlib.animation as anime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from PIL import Image, ImageSequence

fig=plt.figure()
l, =plt.plot([],[],'k-')
l2, = plt.plot([], [], 'm--')
p1, = plt.plot([], [], 'ko')
p2, = plt.plot([], [], 'mo')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')
 
plt.xlim(-5, 5)
plt.ylim(-5, 5)
 
def func(x):
  return np.sin(x)*3
def func2(x):
    return np.cos(x)*3
 
metadata=dict(title="Movie",artist="sourabh")
writer= anime.PillowWriter(fps=15,metadata=metadata)
 
xlist=[]
ylist=[]
ylist2 = []
xlist2 = []
with writer.saving(fig,"sin+cosinewave.gif",100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
 
        l.set_data(xlist,ylist)
        l2.set_data(xlist2,ylist2)
 
        p1.set_data(xval,func(xval))
 
        writer.grab_frame()
    for xval in np.linspace(-5,5,100):
        xlist2.append(xval)
        ylist2.append(func2(xval))
 
        l.set_data(xlist,ylist)
        l2.set_data(xlist2,ylist2)
 
        p2.set_data(xval,func2(xval))
 
        writer.grab_frame()

# bold line is the sine wave. 
# dotted line is the cosine wave.

"""
im = Image.open("sin+cosinewave.gif")

index = 1
for frame in ImageSequence.Iterator(im):
    frame.save("frame%d.gif" % index)
    index += 1
"""