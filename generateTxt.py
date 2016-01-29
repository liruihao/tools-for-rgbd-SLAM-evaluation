#! /usr/bin/python

import os
import os.path

if __name__ == '__main__':
    rgbfile = open('rgb.txt', 'w')
    depfile = open('depth.txt', 'w')
    for parent, dirnames, filenames in os.walk('./rgb/', False):
        time = []
        for filename in filenames:
            time.append( filename[0:len(filename)-4] )
        time.sort()
        for t in time:
            rgbfile.write(t+" rgb/"+t+".png\n")
    rgbfile.close()
    
    for parent, dirnames, filenames in os.walk('./depth/'):
        time = []
        for filename in filenames:
            time.append( filename[0:len(filename)-4] )
        time.sort()
        for t in time:
            depfile.write(t+" depth/"+t+".png\n")
    depfile.close()
    print 'txt file generated.'

