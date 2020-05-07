import carla
import xodrReader
#import rssw
import yaml

xodrReader.load()

fcheck = open("input-check.yaml", "r")
data = fcheck.read()
scheck = yaml.load(data)
print(yaml.dump(scheck))
print(scheck["D1"]["velocity"][0])
print(scheck["D2"]["lane"])
print(scheck["D2"]["velocity"][1])