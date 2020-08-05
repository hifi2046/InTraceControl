import carla
import sys
import rssw
import pickle

n=-1
if(len(sys.argv)==2):
  n=int(sys.argv[1])
print("rssw version:", rssw.version())
f=open("rsscheck.log","rb")
d=pickle.load(f)
f.close()
i=0
for t in d:
#    print(t[0])
#    print(t[1])
#    print(t[2])
    print(i, t[3])
    i+=1
if(n==-1):
  exit(1)
print("extract record %d to input-check.dat" % n)
t=d[n]
lane=rssw.Lane(t[0][0], t[0][1], t[0][2], t[0][3], t[0][4], t[0][5])
ego=rssw.Vehicle(t[1][0], t[1][1], t[1][2], t[1][3])
other=rssw.Vehicle(t[2][0], t[2][1], t[2][2], t[2][3])
print(lane.str())
print(ego.str())
print(other.str())
control = rssw.VControl()
restriction = rssw.Restriction()
rssw.RssCheck(lane, ego, other, restriction)
rssw.RssRestrict(restriction, control)
print(control.str())
print(t[3])
f=open("input-check.dat","w")
tt=[str(x) for x in t[0]]
s=" ".join(tt)
f.write(s+"\n")
tt=[str(x) for x in t[1]]
s=" ".join(tt)
f.write(s+"\n")
tt=[str(x) for x in t[2]]
s=" ".join(tt)
f.write(s+"\n")
f.close()
