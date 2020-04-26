import carla
import matplotlib.pyplot as plt

client = carla.Client("10.140.135.35", 2000)
world = client.get_world()
map = world.get_map()
top = map.get_topology()
warray = [(w[0].transform.location, w[1].transform.location) for w in top]
lines = [([w[0].x, w[1].x], [w[0].y, w[1].y]) for w in warray]
colors = [ "red" if t[0].lane_id > 0 else "blue" for t in top]
labels = ["%d:%d!%d=>%d!%d" % (i, w[0].road_id, w[0].lane_id, w[1].road_id, w[1].lane_id) for (i,w) in zip(range(len(top)),top)]
#for w in warray:
#    print( w[0].x, w[0].y, "=>", w[1].x, w[1].y)
for (line, text, color) in zip(lines, labels, colors):
    plt.plot(line[0], line[1], color)
    plt.text((line[0][0] + line[0][1])/2, (line[1][0] + line[1][1])/2, text)
ax=plt.gca()
ax.invert_xaxis()
plt.show()
