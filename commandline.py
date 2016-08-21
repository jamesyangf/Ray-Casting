import data 

def file_open(argv):
    try:
        file = open(argv,"r")
    except:
        print "error"
        exit()


def eye(argv):
        try:
            for a in range(len(argv)):
                if argv[a] == '-eye':
                    x = float(argv[a+1])
                    y = float(argv[a+2])
                    z = float(argv[a+3])
            return (data.Point(x, y, z))
        except:
            return (data.Point(0.0, 0.0, -14.0))

def view(argv):
        try:
            for b in range(len(argv)):
                if argv[b] == '-view':
                    min_x = float(argv[b+1])
                    max_x = float(argv[b+2])
                    min_y = float(argv[b+3])
                    max_y = float(argv[b+4])
                    width = int(argv[b+5])
                    height = int(argv[b+6])
            return (min_x, max_x, min_y, max_y, width, height)
        except:
            return (-10.0, 10.0, -7.5, 7.5, 1024, 768)


def light(argv):
        try:
            for c in range(len(argv)):
                if argv[c] == '-light':
                    x = float(argv[c+1])
                    y = float(argv[c+2])
                    z = float(argv[c+3])
                    r = float(argv[c+4])
                    g = float(argv[c+5])
                    b = float(argv[c+6])
            return (data.Light(data.Point(x, y, z), data.Color(r, g, b)))
        except:
            return (data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))

def ambient(argv):
        try:
            for d in range(len(argv)):
                if argv[d] == '-ambient':
                    r = float(argv[d+1])
                    g = float(argv[d+2])
                    b = float(argv[d+3])
            return data.Color(r, g, b)
        except:
            return data.Color(1.0, 1.0, 1.0)

                   

def noArgv(argv):
    try:
        x = open(argv,'r')
    except:
        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
    
