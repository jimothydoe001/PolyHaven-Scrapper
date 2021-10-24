import requests
import json
from sys import argv
import wget
import os

UselessVariableNameThatBreaksTheScriptWhenItsNotPresent, qualitytest, fileformat = argv

url = 'https://api.polyhaven.com/assets?t=hdris'
r = requests.get(url)

data = json.loads(r.content)
data.keys()
for hdriname in data.keys():
    print("Downloading:  ")
    print("https://dl.polyhaven.org/file/ph-assets/HDRIs/" + fileformat + "/" + qualitytest + "/" + hdriname + "_" + qualitytest + "." + fileformat + "")
    print("https://cdn.polyhaven.com/asset_img/primary/" + hdriname + ".png")
    downloadthesesrc = ("https://dl.polyhaven.org/file/ph-assets/HDRIs/" + fileformat + "/" + qualitytest + "/" + hdriname + "_" + qualitytest + "." + fileformat + "")
    downloadtheseprev = ("https://cdn.polyhaven.com/asset_img/primary/" + hdriname + ".png")
    os.system("wget -T 15 -c {0}".format(downloadthesesrc, hdriname))
    os.system("wget -T 15 -c {0}".format(downloadtheseprev, hdriname))
    print("/n /n finished downloading" + hdriname)