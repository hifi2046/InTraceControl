from lxml import etree
import math

roadinfo={}
def load():
    global roadinfo
    f=open("map4.xodr", "r")
    d=f.read()
    dd=d.encode('utf-8')
    html=etree.HTML(dd)
    roads=html.xpath('//road')
    for r in roads:
        id = int(r.get("id"))
        length = float(r.get("length"))
    #    print("road %s length %.1f " % ( r.get("id"), float(r.get("length"))), end="")
        for t in r.iter("geometry"):
            x = float(t.get("x"))
            y = float(t.get("y"))
            hdg = float(t.get("hdg"))
    #        print("at:(%.1f, %.1f) hdg %.1f " % (float(t.get("x")), float(t.get("y")), float(t.get("hdg"))), end="")
            break
        w=0
        for t in r.iter("width"):
            w += float(t.get("a"))
    #    print("width %.1f" % w)
        roadinfo[id]=(x, -y, length, w, -hdg*180/math.pi)
