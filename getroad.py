#import rssw
import carla
import rssw
import xodrReader
xodrReader.load()
rinfo = xodrReader.roadinfo
rid = 40
info = rinfo[rid]
print(info)
lid = -4
lane = rssw.Lane(info[0], info[1], info[2], info[3], info[4], lid)
print(lane.str())


