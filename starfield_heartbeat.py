#!/usr/bin/env python
from samplebase import SampleBase
import time
import random
import math

class Starfield(SampleBase):

    global star
    def __init__(self, *args, **kwargs):
        super(Starfield, self).__init__(*args, **kwargs)

    def initxy(self,i,s):
        star[i][0] =  random.randint(-30,30)
        star[i][1] =  random.randint(-30,30)
        star[i][2] =  random.randint(1,255)
        return;

    def run(self):
	global star
        offscreen = self.matrix.CreateFrameCanvas()

	star = [[0]*3 for i in range(300)]
	color = [[0]*3 for i in range(306)]
        x=0	
        for i in range (0,255,5):
	  color[x][0]=0
	  color[x][1]=0
	  color[x][2]=i		
	  x=x+1
        for i in range (0,255):	  
	  color[x][0]=i
	  color[x][1]=i
	  color[x][2]=255-i	
	  x=x+1

	for i in range (0,len(star)):
	  self.initxy(i,star)	

	w=90
	w2=90

        while True:
	  offscreen.Clear()

          ox = 32 + math.cos(2 * math.pi * w/360  ) * 550 ;
          oy = 32 + math.sin(2 * math.pi * w2/360  ) * 20 ;

	  for i in range (0,len(star)): 
            x2 = ((star[i][0]-0) * ((oy)/star[i][2]))+0
            y2 = ((star[i][1]-0) * ((oy)/star[i][2]))+0

            if star[i][2]>1:
     	      star[i][2]=star[i][2]-0.9
   	    else: 
	      self.initxy(i,star)

	    c= int(abs(255-float(star[i][2]))/255*306)
            offscreen.SetPixel(32+x2, 32+y2,color[c][0],color[c][2],color[c][1])

	  if w>360:
	    w=0
	  w=w+0.6
	  if w2>360:
            w2=0
	  w2=w2+2

          offscreen = self.matrix.SwapOnVSync(offscreen)


# Main function
if __name__ == "__main__":
    starField = Starfield()
    if (not starField.process()):
        starField.print_help()
