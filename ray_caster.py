import sys
from cast import *
from commandline import *

def main(argv):
        file = open(argv[1],'r')
        newlist = []
        line = file.readlines()
        for i in line:
                s = i.split()
                if len(s) == 11:
                        try:
                                sphere = data.Sphere(data.Point(float(s[0]),float(s[1]),float(s[2])),float(s[3]),data.Color(float(s[4]),float(s[5]),float(s[6])),data.Finish(float(s[7]),float(s[8]),float(s[9]),float(s[10])))
                                newlist.append(sphere)
                        except:
                                print"malformed sphere on line" "...skipping" 
        return newlist
e = eye(sys.argv)
l = light(sys.argv)
a = ambient(sys.argv)
v = view(sys.argv)
sphere = main(sys.argv)
cast_all_rays(v[0],v[1],v[2],v[3],v[4],v[5],e,sphere,a,l)

if __name__=='__main__':
        main(sys.argv)
